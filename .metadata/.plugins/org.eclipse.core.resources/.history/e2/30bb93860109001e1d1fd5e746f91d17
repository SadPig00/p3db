package com.suwon.ezen.controller;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpSession;

import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.suwon.ezen.mapper.ChannelMapper;
import com.suwon.ezen.mapper.MemberMapper;
import com.suwon.ezen.vo.MemberVO;

import lombok.Setter;

@Controller
@RequestMapping("/")
public class MainController {
	
	@Setter(onMethod_ =@Autowired )
	ChannelMapper mapper;
	
	@Setter(onMethod_ =@Autowired )
	MemberMapper mmapper;
	// 데이터 주기중 가장 초기 데이터 날짜로 검색
	@RequestMapping(value = "/index", method = RequestMethod.GET,produces = "application/text; charset=utf8")
	public String index(Model model) {
		
		Date date1 = mapper.getMinDate();
		Date date2 = mapper.getMinDate();
		String selectedMonth;
		Calendar cal1 = Calendar.getInstance();
		cal1.setTime(date2);
		cal1.add(Calendar.DATE, 1);
		date2 = new Date(cal1.getTimeInMillis());
		SimpleDateFormat simple = new SimpleDateFormat("yyyy-MM-dd");
		String chooseDate1 = simple.format(date1);
		String chooseDate2 = simple.format(date2);
		SimpleDateFormat month = new SimpleDateFormat("M");
		selectedMonth = "6";
		model.addAttribute("channelList", mapper.getChannelList());
		String channel="tilt_01";
		String tilt="tilt_01";
		model.addAttribute("channel",channel);
		model.addAttribute("channelDate", mapper.getDateByChannel(chooseDate1,chooseDate2));
		model.addAttribute("channelData", mapper.getDataByChannel(channel,chooseDate1,chooseDate2));
		model.addAttribute("tempData", mapper.getAvgTemp(chooseDate1, chooseDate2));
		model.addAttribute("battData", mapper.getAvgBatt(chooseDate1, chooseDate2));
		model.addAttribute("avgtilt", mapper.getAvgtilt(channel, chooseDate1, chooseDate2));
		model.addAttribute("maxtilt", mapper.getTiltMaxMin(channel, chooseDate1, chooseDate2).get("maxtilt"));
		model.addAttribute("mintilt", mapper.getTiltMaxMin(channel, chooseDate1, chooseDate2).get("mintilt"));
		model.addAttribute("minDate",chooseDate1);
		model.addAttribute("lat",mapper.getLatLng(tilt).get("lat"));
		model.addAttribute("lng",mapper.getLatLng(tilt).get("lng"));
		model.addAttribute("LatLngList", mapper.getLatLngAll());
		model.addAttribute("minDate",chooseDate1);
		model.addAttribute("countData",mmapper.countMembersByDate(selectedMonth));
		model.addAttribute("selectedMonth",selectedMonth);
		return "index";
	}
	
	//날짜, 채널별로 탐색
	@SuppressWarnings({ "unchecked", "rawtypes" })
	@GetMapping("/channelAjax")
	public ResponseEntity<Map> getChannel(@Param("channel")String channel,@Param("chooseDate")String chooseDate) throws ParseException{
		
		String date1 = chooseDate;
		SimpleDateFormat month = new SimpleDateFormat("M");
		SimpleDateFormat simple = new SimpleDateFormat("yyyy-MM-dd");
		Date date2 = simple.parse(date1);
		Calendar cal1 = Calendar.getInstance();
		cal1.setTime(date2);
		cal1.add(Calendar.DATE, 1);
		date2 = new Date(cal1.getTimeInMillis());
		String chooseDate1 = date1;
		String chooseDate2 = simple.format(date2);
		String tilt=channel;
		Map map = new HashMap<>();
		map.put("channelDate", mapper.getDateByChannel(chooseDate1,chooseDate2));
		map.put("channelData", mapper.getDataByChannel(channel,chooseDate1,chooseDate2));
		map.put("tempData", mapper.getAvgTemp(chooseDate1, chooseDate2));
		map.put("battData", mapper.getAvgBatt(chooseDate1, chooseDate2));
		map.put("avgtilt", mapper.getAvgtilt(channel, chooseDate1, chooseDate2));
		map.put("maxtilt", mapper.getTiltMaxMin(channel, chooseDate1, chooseDate2).get("maxtilt"));
		map.put("mintilt", mapper.getTiltMaxMin(channel, chooseDate1, chooseDate2).get("mintilt"));
		map.put("lat",mapper.getLatLng(tilt).get("lat"));
		map.put("lng",mapper.getLatLng(tilt).get("lng"));
		
		
		return new ResponseEntity<>(map,HttpStatus.OK);
	}
	
	@GetMapping("/login")
	public void login(HttpSession session) {
	}
	@PostMapping("/login")
	public String login(MemberVO vo, Model model, HttpSession session) {
		System.out.println(vo);
		if (vo.getPassword().equals("1234")) {
			mmapper.insertMember(vo);
			session.setAttribute("loginMember",vo);
			return "redirect:/index";
		} else {
			model.addAttribute("msg", "비밀번호가 틀렸습니다.");
			return "alert";
		}
	}
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.removeAttribute("loginMember");
		return "login";
	}
	@GetMapping( value = "/getMonthAjax", produces = "application/json")
	public ResponseEntity<List<Map<String, Object>>> getMonthAjax(String selectedMonth){
		System.out.println(mmapper.countMembersByDate(selectedMonth));
		System.out.println(selectedMonth);
		return new ResponseEntity<List<Map<String, Object>>>(mmapper.countMembersByDate(selectedMonth),HttpStatus.OK);
	}
	
}

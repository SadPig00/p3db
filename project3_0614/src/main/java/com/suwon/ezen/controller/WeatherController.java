package com.suwon.ezen.controller;

import javax.servlet.http.HttpSession;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.suwon.ezen.vo.WeatherVO;

@RestController
@RequestMapping("/sensor")

public class WeatherController {
	static private WeatherVO result;
	@PostMapping(value = "/getData", consumes = "application/json;charset=utf-8",
			produces = "application/json")
	public ResponseEntity<String> getWeather(@RequestBody WeatherVO vo, HttpSession session) {
		System.out.println("들어오나");
		System.out.println(vo);
		result=vo;
		return new ResponseEntity<String>("success",HttpStatus.OK);
	}
	@GetMapping(value = "/resultData", produces = "application/json")
	public ResponseEntity<WeatherVO> resultData(){
		
		return new ResponseEntity<WeatherVO>(result,HttpStatus.OK);
	}
}

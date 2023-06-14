package com.suwon.ezen.mapper;

import java.util.Date;
import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Param;

import com.suwon.ezen.vo.LatLngVO;
public interface ChannelMapper {
	public List<String> getChannelList();
	public List<String> getDataByChannel(@Param("channel")String channel,@Param("chooseDate1")String chooseDate1,@Param("chooseDate2")String chooseDate2);
	public List<String> getDateByChannel(@Param("chooseDate1")String chooseDate1,@Param("chooseDate2")String chooseDate2);
	public String getAvgTemp(@Param("chooseDate1")String chooseDate1,@Param("chooseDate2")String chooseDate2);
	public String getAvgBatt(@Param("chooseDate1")String chooseDate1,@Param("chooseDate2")String chooseDate2);
	public Map<String,Double> getTiltMaxMin(@Param("channel")String channel,@Param("chooseDate1")String chooseDate1,@Param("chooseDate2")String chooseDate2);
	public String getAvgtilt(@Param("channel")String channel,@Param("chooseDate1")String chooseDate1,@Param("chooseDate2")String chooseDate2);
	public Map<String,Double> getLatLng (@Param("tilt") String tilt);
	public List<LatLngVO> getLatLngAll();
	public Date getMinDate();
	
}

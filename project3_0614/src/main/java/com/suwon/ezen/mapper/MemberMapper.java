package com.suwon.ezen.mapper;

import java.util.List;
import java.util.Map;

import com.suwon.ezen.vo.MemberVO;

public interface MemberMapper {
	public void insertMember(MemberVO vo);
	
	public List<Map<String, Object>> countMembersByDate(String selectedMonth);
}
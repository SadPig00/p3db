package com.suwon.ezen.vo;

import java.util.Date;

import lombok.Data;

@Data
public class MemberVO {
	private int pno;
	private String name;
	private String phone;
	private String email;
	private String password;
	private Date logindate;
	private Date selectedMonth;
}

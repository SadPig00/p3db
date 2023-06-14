package com.suwon.ezen.vo;

import java.util.Date;

import lombok.Data;

@Data
public class ChannelVO {
	int tno;
	Date updatetime;
	double tiltData;
	double batt;
	double temp;
}

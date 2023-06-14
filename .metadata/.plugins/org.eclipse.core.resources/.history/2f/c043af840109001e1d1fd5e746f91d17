package com.suwon.ezen.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.context.request.RequestAttributes;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

import com.suwon.ezen.vo.MemberVO;

public class AdminInterceptor extends HandlerInterceptorAdapter {

	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		MemberVO vo= (MemberVO) RequestContextHolder.getRequestAttributes().getAttribute("loginMember", RequestAttributes.SCOPE_SESSION);
		if(vo == null || vo.getName().isEmpty()) {
			request.setAttribute("msg", "관리자만 접근 가능합니다.");
			request.getRequestDispatcher("/WEB-INF/views/alert.jsp").forward(request, response);
			return false;
		}
		return super.preHandle(request, response, handler);
	}
	
}

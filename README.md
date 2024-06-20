# 프로젝트 주제 

맛집 리뷰 커뮤니티

---
# 프로젝트 수행 방향

   1) 회원가입 / 로그인 기능 구현
   2) API 활용 지도에 맛집 표시
   3) 맛집 검색 기능
   4) 맛집 상세페이지 및 후기 작성 기능
   5) 평점 수렴 후 1,2,3위 표시

---
# 프로젝트 수행 도구

__Back-end__
  + Django
  + MySQL
    
__Front-end__
  + HTML
  + CSS
  + JavaScript
  + Bootstrap

---
# 프로젝트 수행 결과

  1) 로그인, 회원가입 페이지

     ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/bde9aec2-b907-4d4a-97bd-8ac5df3fabd6)
     ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/29fdf007-0f1e-4968-9cc7-dd7f8f1daeaa)

  2) 메인 페이지

      ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/ee51125d-7da2-4184-957f-9810c8f0425e)
      + 등록된 맛집 리스트의 순위(평균 평점 기준)가 표시
      + Home = 메인페이지 이동 / List, 리뷰하기 = 맛집 리스트 페이지 이동 / login = 로그인 페이지 (로그인 했다면 logout, mypage 버튼이 뜸) / 리뷰보기 = 해당 가게의 상세페이지 이동
        
  3) 맛집 리스트 페이

      ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/45b6b329-bed0-466b-86e6-f39a2da821cf)
      + 주소와 이름으로 검색 가능
      + 현 페이지에 있는 식당이 지도에 마커와 함께 표시됨
      + 마커의 파란 화살표를 눌러 해당 가게의 상세페이지로 이동
      + 가게는 5개씩 페이징, 검색 후 결과가 5개 이상이면 페이징 사용 가능
      + 페이징은 현 페이지에서 +-2개씩 표시됨
  
  4) 맛집 상세 페이지
  
      ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/d26bc1a9-bc55-4f3e-b528-2333524288be)
      + 상세 정보와 평점 등록된 후기가 보임
      + 후기를 등록할 수 있는 후기 작성 버튼이 있음 (후기 작성을 위해서는 로그인이 필수, 로그인이 안되어 있다면 로그인 페이지로 이동)
  
  6) 후기 작성 페이지
  
      ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/003bbd84-9d4c-4e4a-90cd-6121facd03af)
      + 후기 글을 작성할 수 있는 텍스트 필드가 있고 평점 1~5점으로 선택 가능
      + 작성 완료하면 DB로 들어감
     
  8) 마이페이지
 
       ![image](https://github.com/Kim-yerin0904/multicam_interface_project/assets/77713307/91bde441-4f71-41ce-9038-0e4a3544bc7d)
       + 회원 정보와 최근에 작성한 후기를 확인할 수 있음

   

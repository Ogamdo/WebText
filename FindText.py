import requests
from bs4 import BeautifulSoup

# 웹사이트 주소 입력
url = input("텍스트를 긁어올 웹 사이트의 주소를 입력해주세요: ")
output_file = input("저장할 파일의 이름을 입력해주세요: ") # 저장할 파일 이름

try:
    # 웹 페이지 요청
    response = requests.get(url)
    response.raise_for_status()  # 요청 에러 처리

    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # <p> 태그 텍스트 추출
    paragraphs = soup.find_all('p')

    # <p> 태그 텍스트를 출력 및 파일로 저장
    with open(output_file, "w", encoding="utf-8") as file:
        for idx, p in enumerate(paragraphs, 1):
            text = p.get_text(strip=True)  # 텍스트만 추출
            print(f"{idx}. {text}")  # 콘솔에 출력
            file.write(f"{idx}. {text}\n")  # 파일에 저장
            file.write("\n")  # 줄 간격 추가

    print(f"<p> 태그의 내용이 '{output_file}' 파일에 저장되었습니다!")

except requests.exceptions.RequestException as e:
    print(f"파싱 불가, 오류: {e}")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")

import fastapi
from fastapi import Request
from model import generate_question

app = fastapi.FastAPI()

@app.post("/test")
async def test(request: Request):
    split_text_list = []
    input_data = await request.json()

    # 텍스트만 파싱
    context = input_data["context"]

    # 텍스트 문단 나누기
    if len(context) > 30:
        text_list = context.split('.')
    else:
        text_list = [context]
    # 함수에 적용
    for i in range(len(text_list)-1):
        result = generate_question(text_list[i])
        split_text_list.append(result)
        print(split_text_list[i])
    # return generate_question(context)
    return split_text_list

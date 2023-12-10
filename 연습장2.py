from collections import deque

def largestRectangleArea(heights):
    stack = deque()
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1][0]]:
            height, index = stack.pop()
            width = i if not stack else i - stack[-1][1] - 1
            max_area = max(max_area, height * width)

        stack.append((heights[i], i))

    while stack:
        height, index = stack.pop()
        width = len(heights) if not stack else len(heights) - stack[-1][1] - 1
        max_area = max(max_area, height * width)

    return max_area

if __name__ == "__main__":
    n = int(input("빌딩 수를 입력하세요: "))
    building_heights = list(map(int, input("빌딩의 높이를 차례로 입력하세요: ").split()))

    result = largestRectangleArea(building_heights)
    print(f"스카이라인 아래에 있는 가장 큰 직사각형의 면적: {result}")

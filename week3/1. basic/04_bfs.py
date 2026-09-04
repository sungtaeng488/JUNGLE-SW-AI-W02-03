"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []
    que = deque([])
    #만약 그래프 맨 밑으로 가면?
    if len(visited) == len(graph):
        return visited
    for i in range(len(graph)):
        if len(que) == start:
            que.append(start)
        else:
            # 근데 그 키 값들에 대한 value 값들을 다 뺴야하는데 어케 뺄ㄱ
            # 만약 그 키에 대한 value값들이 이미 visited에 있으면 다음으로 넘어가고 그렇지 않으면 그 값들을 넣는다.
            for ch in graph[i-1]:
                if ch in que:
                    continue
                else:
                    que.append(ch)
    while len(que) != 0:
        b = que.popleft()
        visited.append(b)
    return visited

        


    

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


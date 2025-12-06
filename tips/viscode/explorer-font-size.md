# Antigravity (VS Code) Explorer Font Size Adjustment

Antigravity 에디터(VS Code 기반)에서 **Explorer(탐색기)의 폰트 크기만 따로 조절하는 설정은 기본적으로 제공되지 않습니다.**

대신 전체 UI의 배율을 조절하여 Explorer의 글자 크기를 키울 수 있습니다.

## 1. 단축키 사용 (가장 빠름)
전체 화면의 확대/축소를 통해 탐색기 글씨 크기를 조절할 수 있습니다.
*   **확대**: `Cmd` + `+` (맥)
*   **축소**: `Cmd` + `-` (맥)
*   **초기화**: `Cmd` + `0` (맥)

## 2. 설정(Settings) 변경
설정 메뉴에서 줌 레벨을 고정할 수 있습니다.
1. `Cmd` + `,` 를 눌러 **Settings**를 엽니다.
2. 검색창에 `window.zoomLevel`을 검색합니다.
3. 값을 1, 2 등으로 높여서 전체 UI 크기를 키웁니다. (기본값은 0)

> **참고:** `Editor: Font Size` 설정은 코드 편집 영역의 폰트 크기만 변경하며, 사이드바(Explorer)에는 영향을 주지 않습니다.

import flet as ft
import json


def main(page: ft.Page):
    # ページ設定
    page.title = "天気予報"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = "auto"

    # JSONデータを読み込み
    with open("areas.json", "r", encoding="utf-8") as file:
        areas_data = json.load(file)  # 全体データを読み込む

    # 地域を取得 ("centers" キー内のデータを利用)
    centers = areas_data["centers"]

# 詳細情報を表示するためのテキスト
    details = ft.Text(value="ここに選択した地域の詳細が表示されます。", size=16)


    # 地域選択時のイベントハンドラ
    def show_details(e):
        center_key = e.control.data  # 選択した地域のキー
        center_data = centers[center_key]  # 選択した地域のデータ
        detail_text = json.dumps(center_data, ensure_ascii=False, indent=2)
        details.value = f"【{center_data['name']}】\n\n{detail_text}"
        page.update()

    # 地域リストを作成
    list_view = ft.ListView(expand=1, spacing=10, padding=10)
    for center_key, center_data in centers.items():
        list_view.controls.append(
            ft.ListTile(
                title=ft.Text(center_data["name"], size=18),
                on_click=show_details,
                data=center_key,  # 地域キーを保存
            )
        )

    # ページのレイアウトを構築
    page.add(
        ft.AppBar(title=ft.Text("天気予報"), bgcolor=ft.colors.BLUE),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("地域を選択", size=20, weight="bold"),
                        list_view,
                    ],
                    width=300,
                    spacing=20,
                ),
                ft.VerticalDivider(width=1),
                ft.Column(
                    [
                        ft.Text("詳細情報", size=20, weight="bold"),
                        details,
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)

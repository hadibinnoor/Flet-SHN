import flet as ft

def to_sit(att, total_hour):
    present = (att*total_hour)/100
    k=1
    while att<75:
        att= ((present+k)/(total_hour+k))*100
        k=k+1
    return k+1

def main(page):
    def btn_click(e):
        if not txt_att.value:
            txt_att.error_text = "Please enter your name"
            page.update()
        else:
            att = int(txt_att.value)
            total_hour = int(txt_totalhour.value)
            page.clean()
            page.add(ft.Text(to_sit(att, total_hour)))
            

    txt_att = (ft.TextField(label="Enter your Attendance"))
    txt_totalhour = (ft.TextField(label="Total Attendance Marked"))

    page.add(txt_att,txt_totalhour, ft.ElevatedButton("Calculate to sit", on_click=btn_click))

ft.app(target=main)
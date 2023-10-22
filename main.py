import flet as ft

def to_sit(att, total_hour, perc):
    present = (att*total_hour)/100
    k=0
    while att<perc:
        att= ((present+k)/(total_hour+k))*100
        k=k+1
    return k

def main(page):
    def btn_click(e):
        if not txt_att.value:
            txt_att.error_text = "Please enter the attendance"
            page.update()
        elif not txt_totalhour.value:
            txt_totalhour.error_text = "Please enter the total hours marked"
            page.update()
        elif not txt_perc.value:
            txt_perc.error_text = "Please enter your desired attendance percentage"
            page.update()
        else:
            att = int(txt_att.value)
            total_hour = int(txt_totalhour.value)
            perc = int(txt_perc.value)
            page.clean()
            textmess = ft.Text("The number of hours you should attend : ", weight="bold", size="25")
            ps = "ps: make sure you don't get any absent marked in between"
            page.add(textmess,ft.Text(to_sit(att, total_hour,perc), weight="bold",size = "35"), ft.Text(ps))
            
    txt_att = (ft.TextField(label="Enter your Attendance"))
    txt_totalhour = (ft.TextField(label="Total Attendance Marked"))
    txt_perc = (ft.TextField(label="Desired attendance percentage (can't be 100)"))

    page.add(txt_att,txt_totalhour,txt_perc, ft.ElevatedButton("Calculate the number of hours to attend", on_click=btn_click))

ft.app(target=main)

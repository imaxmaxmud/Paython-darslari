import pygal

line_chart=pygal.Line()
line_chart.title="Statistika"
line_chart.x_labels=['January','February','March','April']
line_chart.add("Facebook",[9.24,13.7,16.24])
line_chart.add("Youtube",[10.45,4.78,12.12])
line_chart.add("Instagram",[1.1,2.2,3.3])
line_chart.render_in_browser()
from fpdf import FPDF
import os
pdf = FPDF()
pdf.set_margins(40,40,40)
pdf.add_page()
pdf.set_font('Arial', 'B', 36)
pdf.set_y(90)
pdf.set_x(50)
pdf.cell(150, 20, 'CAR DAMAGE REPORT', 1, 0, 'C')
pdf.set_y(170)
pdf.set_x(170)
pdf.set_font('Arial', 'B', 16)
pdf.cell(10, 20, 'Surya E', 0, 2, 'R')
pdf.cell(10, 20, 'Tanuja K', 0, 2, 'R')
pdf.add_page()
pdf.write(5, 'The scratch detected at \n ')
for name in os.listdir('output'):
        if name.endswith("jpg"):
                pdf.add_page()
                filename='output/'+name
                pdf.image(filename, x = 10, y = 90, w=150, h=84)
pdf.output('report.pdf', 'F')

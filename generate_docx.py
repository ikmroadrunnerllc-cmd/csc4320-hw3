import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_docx():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    with open('Homework3_Answers.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    for line in lines:
        if line.startswith('====='):
            continue
        elif line.startswith('-----'):
            continue
        elif 'GEORGIA STATE UNIVERSITY' in line:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(line)
            r.bold = True
            r.font.size = Pt(14)
            r.font.color.rgb = RGBColor(0, 51, 102)
        elif 'Operating Systems - Homework 3 Solutions' in line:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(line)
            r.bold = True
            r.font.size = Pt(13)
        elif line.startswith('Student:') or line.startswith('Instructor:') or line.startswith('Chapters'):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(line)
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(100, 100, 100)
        elif line.startswith('CONCURRENCY AND') or line.startswith('SYNCHRONIZATION AND') or line.startswith('DEADLOCK AVOIDANCE'):
            doc.add_paragraph()
            h = doc.add_heading(line, level=1)
            h.runs[0].font.size = Pt(13)
            h.runs[0].font.color.rgb = RGBColor(180, 50, 20)
        elif line.startswith('Question '):
            h = doc.add_heading(line, level=2)
            h.runs[0].font.size = Pt(11.5)
            h.runs[0].font.color.rgb = RGBColor(0, 51, 102)
        elif line.startswith('(a)') or line.startswith('(b)') or line.startswith('(c)'):
            p = doc.add_paragraph()
            r = p.add_run(line)
            r.bold = True
            r.font.size = Pt(10.5)
        elif line.strip() == '':
            doc.add_paragraph()
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(line)
            if 'wait(' in line or 'signal(' in line or 'lock(' in line or 'P0 ' in line or 'Allocation' in line:
                r.font.name = 'Consolas'
                r.font.size = Pt(9)
            else:
                r.font.name = 'Calibri'
                r.font.size = Pt(10)

    doc.save('Homework3_Answers.docx')
    print('Homework3_Answers.docx created successfully')

if __name__ == '__main__':
    create_docx()

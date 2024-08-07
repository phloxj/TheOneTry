from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from reportlab.lib.pagesizes import letter
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from natsort import natsorted
from pdf import Ui_Form
from PIL import Image
import os


def change_extension(directory, old_extension, new_extension):
    for filename in os.listdir(directory):
        # 检查文件名是否以旧扩展名结尾
        if filename.endswith(old_extension):
            # 构造新的文件名
            new_filename = filename[:-len(old_extension)] + new_extension
            # 构造旧文件和新文件的完整路径
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)


def dismantle(pdf_path, png_name):
    # 将PDF转换为PNG图片列表
    images = convert_from_path(pdf_path)

    # 分割路径，获取文件夹路径和文件名
    folder_path, _ = os.path.split(pdf_path)

    # 保存
    image_folder = folder_path + "/" + png_name
    print(image_folder)
    # 检查文件夹是否存在
    if not os.path.exists(image_folder):
        # 文件夹不存在，创建文件夹
        os.makedirs(image_folder)
    for i, image in enumerate(images):
        image_path = image_folder + f'\\page_{i}.png'
        image.save(image_path, 'PNG')

    return image_folder


def convert_png_to_pdf(png_folder, pdf_path):
    # 检索指定文件夹中所有以.png为后缀的文件，并进行自然排序
    images = natsorted([img for img in os.listdir(png_folder) if img.endswith(".png")])

    # 创建一个PDF画布，同时指定PDF文件的保存路径和页面大小
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # 遍历并处理每一张图片
    for image_name in images:
        image_path = os.path.join(png_folder, image_name)
        img = Image.open(image_path)
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height

        # 根据图片的宽高比调整其大小，以适应PDF页面
        if aspect_ratio > 1:
            img_width = width
            img_height = width / aspect_ratio
        else:
            img_height = height
            img_width = height * aspect_ratio

            # 为PDF页面设置新的大小
        c.setPageSize((img_width, img_height))

        # 在PDF页面上绘制图片
        c.drawImage(image_path, 0, 0, width=img_width, height=img_height)

        # 在PDF中添加新页面
        c.showPage()

        # 保存PDF文件
    c.save()


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pushButton_choice1.clicked.connect(self.getPath1)
        self.pushButton_choice2.clicked.connect(self.getPath2)
        self.pushButton_choice3.clicked.connect(self.getPath3)
        self.pushButton_png2pdf.clicked.connect(self.enter1)
        self.pushButton_pdf2png.clicked.connect(self.enter2)
        self.pushButton_NameChange.clicked.connect(self.enter3)

    def getPath1(self):
        file_path1, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "png Files (*.png)")
        folder_path1, file_name1 = os.path.split(file_path1)
        self.lineEdit_choice1.setText(folder_path1)
        input_name1 = file_name1.split(".")[0] + ".pdf"
        self.lineEdit_input1.setText(input_name1)

    def getPath2(self):
        file_path2, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "pdf Files (*.pdf)")
        self.lineEdit_choice2.setText(file_path2)
        _, file_name2 = os.path.split(file_path2)
        input_name2 = file_name2.split(".")[0]
        self.lineEdit_input2.setText(input_name2)

    def getPath3(self):
        file_path3, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "All Files (*)")
        folder_path3, _ = os.path.split(file_path3)
        self.lineEdit_choice3.setText(folder_path3)
        old_exname = '.' + file_path3.split('.')[1]
        self.lineEdit_oldname.setText(old_exname)

    def enter1(self):
        png = self.lineEdit_choice1.text()
        pdf = self.lineEdit_input1.text()
        pdf_path = png + "/" + pdf
        convert_png_to_pdf(png, pdf_path)
        self.lineEdit_output1.setText(pdf_path)

    def enter2(self):
        pdf = self.lineEdit_choice2.text()
        png = self.lineEdit_input2.text()
        output_name2 = dismantle(pdf, png)
        self.lineEdit_output2.setText(output_name2)

    def enter3(self):
        file_path = self.lineEdit_choice3.text()
        old_exname = self.lineEdit_oldname.text()
        new_exname = self.lineEdit_newname.text()
        change_extension(file_path, old_exname, new_exname)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

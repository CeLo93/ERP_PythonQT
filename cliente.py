# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# IMPORT icons
import icon_retornar
import icon_pesquisar
import icon_geral
import icon_excluir
import icon_consultar
import icon_alterar
import icon_adicionar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem

# LIBS DIVERSAS

import mysql.connector
import pandas as pd

# IMPORT FORM SISTEMAS#
from dadosCliente import Ui_formdadosCliente

# IMPORT DAS VARIAVEIS CONTROLE
import variaveisControle

# VARIAVEIS CONEXÃO COM BD
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database

# ----------------------------------------------------------------


class Ui_formCliente(object):
    def setupUi(self, formCliente):
        formCliente.setObjectName("formCliente")
        formCliente.resize(651, 391)
        self.bt_adicionar = QtWidgets.QPushButton(formCliente)
        self.bt_adicionar.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.bt_adicionar.setStyleSheet(
            "image:url(:/icon_adicionar/Icons/adicionar.png)")
        self.bt_adicionar.setText("")
        self.bt_adicionar.setObjectName("bt_adicionar")
        self.bt_alterar = QtWidgets.QPushButton(formCliente)
        self.bt_alterar.setGeometry(QtCore.QRect(70, 0, 71, 71))
        self.bt_alterar.setStyleSheet(
            "image:url(:/icon_alterar/Icons/alterar.png)")
        self.bt_alterar.setText("")
        self.bt_alterar.setObjectName("bt_alterar")
        self.bt_consultar = QtWidgets.QPushButton(formCliente)
        self.bt_consultar.setGeometry(QtCore.QRect(140, 0, 71, 71))
        self.bt_consultar.setStyleSheet(
            "image:url(:/icon_consultar/Icons/consultar.png)")
        self.bt_consultar.setText("")
        self.bt_consultar.setObjectName("bt_consultar")
        self.bt_excluir = QtWidgets.QPushButton(formCliente)
        self.bt_excluir.setGeometry(QtCore.QRect(210, 0, 71, 71))
        self.bt_excluir.setStyleSheet(
            "image:url(:/icon_excluir/Icons/excluir.png)")
        self.bt_excluir.setText("")
        self.bt_excluir.setObjectName("bt_excluir")
        self.bt_retornar = QtWidgets.QPushButton(formCliente)
        self.bt_retornar.setGeometry(QtCore.QRect(580, 0, 61, 61))
        self.bt_retornar.setStyleSheet(
            "image:url(:/icon_retornar/Icons/retornar.png)")
        self.bt_retornar.setText("")
        self.bt_retornar.setObjectName("bt_retornar")
        self.bt_pesquisar = QtWidgets.QPushButton(formCliente)
        self.bt_pesquisar.setGeometry(QtCore.QRect(490, 110, 31, 21))
        self.bt_pesquisar.setStyleSheet(
            "image: url(:/icon_pesquisar/Icons/pesquisar.png)")
        self.bt_pesquisar.setText("")
        self.bt_pesquisar.setObjectName("bt_pesquisar")
        self.tb_cliente = QtWidgets.QTableWidget(formCliente)
        self.tb_cliente.setGeometry(QtCore.QRect(10, 150, 631, 231))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.tb_cliente.setFont(font)
        self.tb_cliente.setObjectName("tb_cliente")
        self.tb_cliente.setColumnCount(4)
        self.tb_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(3, item)
        self.lb_nomeCliente = QtWidgets.QLabel(formCliente)
        self.lb_nomeCliente.setGeometry(QtCore.QRect(50, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_nomeCliente.setFont(font)
        self.lb_nomeCliente.setObjectName("lb_nomeCliente")
        self.txt_nomeCliente = QtWidgets.QLineEdit(formCliente)
        self.txt_nomeCliente.setGeometry(QtCore.QRect(170, 110, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.txt_nomeCliente.setFont(font)
        self.txt_nomeCliente.setText("")
        self.txt_nomeCliente.setObjectName("txt_nomeCliente")
        self.bt_pesquisarGeral = QtWidgets.QPushButton(formCliente)
        self.bt_pesquisarGeral.setGeometry(QtCore.QRect(520, 110, 21, 21))
        self.bt_pesquisarGeral.setStyleSheet(
            "image: url(:/icon_geral/Icons/filtro.png)")
        self.bt_pesquisarGeral.setText("")
        self.bt_pesquisarGeral.setObjectName("bt_pesquisarGeral")

        self.retranslateUi(formCliente)
        QtCore.QMetaObject.connectSlotsByName(formCliente)

    def retranslateUi(self, formCliente):
        _translate = QtCore.QCoreApplication.translate
        formCliente.setWindowTitle(_translate("formCliente", "Form"))
        self.bt_adicionar.setToolTip(_translate(
            "formCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_alterar.setToolTip(_translate(
            "formCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_consultar.setToolTip(_translate(
            "formCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_excluir.setToolTip(_translate(
            "formCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_retornar.setToolTip(_translate(
            "formCliente", "<html><head/><body><p><br/></p></body></html>"))
        item = self.tb_cliente.horizontalHeaderItem(0)
        item.setText(_translate("formCliente", "ID"))
        item = self.tb_cliente.horizontalHeaderItem(1)
        item.setText(_translate("formCliente", "Nome"))
        item = self.tb_cliente.horizontalHeaderItem(2)
        item.setText(_translate("formCliente", "Telefone"))
        item = self.tb_cliente.horizontalHeaderItem(3)
        item.setText(_translate("formCliente", "Cidade"))
        self.lb_nomeCliente.setText(_translate("formCliente", "Nome Cliente:"))

# ----------------------------------------------------------------v
        # BOTÕES SISTEMA
        self.bt_retornar.clicked.connect(lambda: self.sairTela(formCliente))
        self.bt_pesquisarGeral.clicked.connect(self.pesquisarGeral)
        self.bt_pesquisar.clicked.connect(self.pesquisarCliente)
        self.bt_adicionar.clicked.connect(self.cadastrarCliente)
        self.bt_consultar.clicked.connect(self.consultarCliente)
        self.bt_alterar.clicked.connect(self.alterarCliente)
        self.bt_excluir.clicked.connect(self.excluirCliente)

# ----------------------------------------------------------------^


# ----------------------------------------------------------------

    # FUNÇÕES SISTEMA ----------------------------------------------------------------v

    def sairTela(self, formCliente):
        variaveisControle.tipoTelaDadosCliente == ''
        formCliente.close()

    # Consulta tabela Banco de dados:
    # - Conexão com o BD
    def pesquisarGeral(self):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM cliente')
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns=[
            'ID', 'Nome', 'Telefone', 'Cidade'])
        self.all_data = df

        # Carrega o arquivo na tabela tb_cliente (faz uma tabela real)
        numRows = len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        # Colocando as infos nas linhas interando
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()
        # Encerra consulta ao BD
        mycursor.close()

    # PESQUISAR NOME CLIENTE
    def pesquisarCliente(self):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        mycursor = mydb.cursor()
        nomeConsulta = self.txt_nomeCliente.text()
        consultaSQL = "SELECT * FROM cliente WHERE Nome LIKE '" + nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns=[
            'ID', 'Nome', 'Telefone', 'Cidade'])
        self.all_data = df
        # Carrega o arquivo na tabela tb_cliente (faz uma tabela real)
        numRows = len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)
        # Colocando as infos nas linhas interando
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()
        # Encerra consulta ao BD
        mycursor.close()

    # FUNÇÃO CADSTRAR CLIENTE
    def cadastrarCliente(self):
        variaveisControle.tipoTelaDadosCliente = 'incluir'
        self.formdadosCliente = QtWidgets.QWidget()
        self.ui = Ui_formdadosCliente()
        self.ui.setupUi(self.formdadosCliente)
        self.formdadosCliente.show()

    # FUNÇÃO consultarCliente
    def consultarCliente(self):
        variaveisControle.tipoTelaDadosCliente = 'consultar'
        # Id de cliente para consulta
        line = self.tb_cliente.currentRow()
        # '0' é o ID do cliente, pois eu quero pegá-lo por ser único
        item = self.tb_cliente.item(line, 0)
        if item is not None:
            variaveisControle.idConsulta = item.text()
            # Abertura da tela consultaCliente
            self.formdadosCliente = QtWidgets.QWidget()
            self.ui = Ui_formdadosCliente()
            self.ui.setupUi(self.formdadosCliente)
            self.formdadosCliente.show()

    # FUNÇÃO alterarCliente
    def alterarCliente(self):
        variaveisControle.tipoTelaDadosCliente = 'alterar'
        # Id de cliente para consulta
        line = self.tb_cliente.currentRow()
        # '0' é o ID do cliente, pois eu quero pegá-lo por ser único
        item = self.tb_cliente.item(line, 0)
        if item is not None:
            variaveisControle.idConsulta = item.text()
            # Abertura da tela consultaCliente
            self.formdadosCliente = QtWidgets.QWidget()
            self.ui = Ui_formdadosCliente()
            self.ui.setupUi(self.formdadosCliente)
            self.formdadosCliente.show()

    # FUNÇÃO excluirCliente
    def excluirCliente(self):

        # Id de cliente para consulta para fins de exclusão
        line = self.tb_cliente.currentRow()
        # '0' é o ID do cliente, pois eu quero pegá-lo por ser único
        item = self.tb_cliente.item(line, 0)
        if item is not None:

            idCliente = item.text()
            # Conexão com o bd
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            mycursor = mydb.cursor()
            sql = " DELETE FROM cliente WHERE IdCliente = '" + idCliente + "'"
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, 'record(s) exclused')

            # Atualizar tabela com a consulta completa
            mycursor.execute('SELECT * FROM cliente')
            myresult = mycursor.fetchall()
            df = pd.DataFrame(myresult, columns=[
                'ID', 'Nome', 'Telefone', 'Cidade'])
            self.all_data = df
            # Carrega o arquivo na tabela tb_cliente (faz uma tabela real)
            numRows = len(self.all_data.index)
            self.tb_cliente.setColumnCount(len(self.all_data.columns))
            self.tb_cliente.setRowCount(numRows)
            self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)
            # Colocando as infos nas linhas interando
            for i in range(numRows):
                for j in range(len(self.all_data.columns)):
                    self.tb_cliente.setItem(
                        i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
            self.tb_cliente.resizeColumnsToContents()
            self.tb_cliente.resizeRowsToContents()
            # Encerra consulta ao BD
            mycursor.close()


# ----------------------------------------------------------------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formCliente = QtWidgets.QWidget()
    ui = Ui_formCliente()
    ui.setupUi(formCliente)
    formCliente.show()
    sys.exit(app.exec_())

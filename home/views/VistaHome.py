from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QComboBox, QGridLayout, QLabel, QSpacerItem, QHBoxLayout
from PyQt5.QtCore import Qt

from calendario.Calendario import Calendario
from dipendente.controller.ControlloreDipendente import ControlloreDipendente
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listamovimenti.views.VistaListaMovimenti import VistaListaMovimenti


class VistaHome(QWidget):
    selezione_campo = None
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        #self.setFixedSize(1250, 700)
        self.showMaximized()
        from home.login.Login import Login
        self.controller = ControlloreDipendente(Login.accesso_utente)
        # layout a griglia per la pagina
        self.layout_admin = QGridLayout()
        self.layout_pt = QHBoxLayout()
        self.layout_collab = QHBoxLayout()
        self.layout_admin.setAlignment(Qt.AlignCenter)
        self.layout_pt.setAlignment(Qt.AlignCenter)
        self.layout_collab.setAlignment(Qt.AlignCenter)
        self.layout_admin.setSpacing(25)
        self.layout_pt.setSpacing(25)
        self.layout_collab.setSpacing(25)
        # lista dei campi presenti nel centro polisportivo
        self.lista_campi = ["Calcio", "Calcetto", "Tennis", "Paddle"]
        # inserimento sfondo
        image = QLabel(self)
        pixmap = QPixmap("home/views/centro.png")
        image.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())
        image.show()
        # costruttore condizionale
        if Login.autorizzazione_accesso == "Amministratore":
            self.setWindowTitle("Home - Amministratore")
            # VISTA HOME AMMINISTRATORE
            self.layout_admin.addWidget(QLabel("<font size = '6'> <b><u> Bentornato nell'area amministratore! </b></u> </font>"), 0, 0, 1, 2)
            self.layout_admin.addWidget(QLabel("<font size = '5'> <b> Selezionare l'attività da svolgere </b> </font>"),1, 0)
            self.layout_admin.addWidget(QLabel("<font size = '4'> <b> Gestisci prenotazioni campi da gioco </b> </font>"), 2, 0)
            self.layout_admin.addWidget(self.get_combo(self.lista_campi), 2, 1)
            self.layout_admin.addWidget(QLabel("<font size = '4'> <b> Gestisci i dipendenti del tuo centro </b> </font>"), 3, 0)
            self.layout_admin.addWidget(self.pulsante_con_nome("Gestione dipendenti", self.go_lista_dipendenti), 3, 1)
            self.layout_admin.addWidget(QLabel("<font size = '4'> <b> Gestisci i clienti della palestra </b> </font>"), 4, 0)
            self.layout_admin.addWidget(self.pulsante_con_nome("Gestione Palestra", self.go_gestione_palestra), 4, 1)
            self.layout_admin.addWidget(QLabel("<font size = '4'> <b> Gestisci i movimenti di cassa </b> </font>"), 5, 0)
            self.layout_admin.addWidget(self.pulsante_con_nome("Gestione movimenti cassa", self.go_gestione_cassa), 5, 1)
            self.layout_admin.addWidget(self.pulsante_con_nome("Esci", self.funz_esci), 6, 2)
            self.setLayout(self.layout_admin)
        elif Login.autorizzazione_accesso == "Personal Trainer":
            self.setWindowTitle("Home - Personal Trainer")
            # VISTA HOME PERSONAL TRAINER
            v_lay_dip_sx = QVBoxLayout()
            v_lay_dip_dx = QVBoxLayout()
            v_lay_dip_esci = QVBoxLayout()
            v_lay_dip_sx.addStretch()
            v_lay_dip_sx.addWidget(QLabel("<font size = '6'> <b><u> Bentornato nell'area dipendente! </b></u> </font>"))
            v_lay_dip_sx.addStretch()
            v_lay_dip_sx.addWidget(QLabel("<font size = '5'> <b> I tuoi dati: </b> </font>"))
            v_lay_dip_sx.addWidget(self.get_label_info("Nome", self.controller.get_nome_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Cognome", self.controller.get_cognome_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Nato a ", self.controller.get_luogo_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("il", self.controller.get_data_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Email", self.controller.get_email_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Abilitazione", self.controller.get_abilitazione_dipendente()))
            v_lay_dip_sx.addStretch()
            v_lay_dip_dx.addStretch()
            v_lay_dip_dx.addWidget(QLabel("<font size = '5'> <b> Le tue attività: </b> </font>"))
            v_lay_dip_dx.addWidget(QLabel("<font size = '4'> <b> Gestisci prenotazione campi: </b> </font>"))
            v_lay_dip_dx.addWidget(self.get_combo(self.lista_campi))
            v_lay_dip_dx.addWidget(QLabel("<font size = '4'> <b> Gesisci clienti della palestra: </b> </font>"))
            v_lay_dip_dx.addWidget(self.pulsante_con_nome("Gestione Palestra", self.go_gestione_palestra))
            v_lay_dip_dx.addStretch()
            v_lay_dip_esci.addStretch()
            v_lay_dip_esci.addWidget(self.pulsante_con_nome("Esci", self.funz_esci))
            self.layout_pt.addLayout(v_lay_dip_sx)
            self.layout_pt.addItem(QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Minimum))
            self.layout_pt.addLayout(v_lay_dip_dx)
            self.layout_pt.addItem(QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Minimum))
            self.layout_pt.addLayout(v_lay_dip_esci)
            self.setLayout(self.layout_pt)
        elif Login.autorizzazione_accesso == "Collaboratore":
            self.setWindowTitle("Home - Collaboratore")
            # VISTA HOME COLLABORATORE
            v_lay_dip_sx = QVBoxLayout()
            v_lay_dip_dx = QVBoxLayout()
            v_lay_dip_esci = QVBoxLayout()
            v_lay_dip_sx.addStretch()
            v_lay_dip_sx.addWidget(QLabel("<font size = '6'> <b><u> Bentornato nell'area dipendente! </b></u> </font>"))
            v_lay_dip_sx.addStretch()
            v_lay_dip_sx.addWidget(QLabel("<font size = '5'> <b> I tuoi dati: </b> </font>"))
            v_lay_dip_sx.addWidget(self.get_label_info("Nome", self.controller.get_nome_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Cognome", self.controller.get_cognome_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Nato a ", self.controller.get_luogo_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("il", self.controller.get_data_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Email", self.controller.get_email_dipendente()))
            v_lay_dip_sx.addWidget(self.get_label_info("Abilitazione", self.controller.get_abilitazione_dipendente()))
            v_lay_dip_sx.addStretch()
            v_lay_dip_dx.addStretch()
            v_lay_dip_dx.addWidget(QLabel("<font size = '5'> <b> Le tue attività: </b> </font>"))
            v_lay_dip_dx.addWidget(QLabel("<font size = '4'> <b> Gestisci prenotazione campi: </b> </font>"))
            v_lay_dip_dx.addWidget(self.get_combo(self.lista_campi))
            v_lay_dip_dx.addWidget(QLabel("<font size = '4'> <b> Gesisci clienti della palestra: </b> </font>"))
            v_lay_dip_dx.addWidget(self.pulsante_con_nome("Gestione Palestra", self.go_gestione_palestra))
            v_lay_dip_dx.addWidget(QLabel("<font size = '4'> <b> Gesisci movimenti di cassa: </b> </font>"))
            v_lay_dip_dx.addWidget(self.pulsante_con_nome("Gestione movimenti cassa", self.go_gestione_cassa))
            v_lay_dip_dx.addStretch()
            v_lay_dip_esci.addStretch()
            v_lay_dip_esci.addWidget(self.pulsante_con_nome("Esci", self.funz_esci))
            self.layout_collab.addLayout(v_lay_dip_sx)
            self.layout_collab.addItem(QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Minimum))
            self.layout_collab.addLayout(v_lay_dip_dx)
            self.layout_collab.addItem(QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Minimum))
            self.layout_collab.addLayout(v_lay_dip_esci)
            self.setLayout(self.layout_collab)

    # metodo che legge la selezione della combobox
    def get_combo(self, lista_campi):
        self.combo_campo = QComboBox()
        combo_model = QStandardItemModel(self.combo_campo)
        combo_model.appendRow(QStandardItem("Gestione campi"))
        for campo in lista_campi:
            combo_model.appendRow(QStandardItem(campo))
        self.combo_campo.activated.connect(self.go_gestione_campi)
        self.combo_campo.setModel(combo_model)
        self.combo_campo.setStyleSheet("background-color: #add8e6; font-size: 15px; font-weight: bold;")
        return self.combo_campo

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format('<b>{}</b>'.format(testo), valore))
        font_nome = current_label.font()
        current_label.setFont(font_nome)
        current_font = current_label.font()
        current_font.setPointSize(18)
        current_label.setFont(current_font)
        return current_label

    # metodo che definisce la costruzione di un bottone con il suo titolo
    def pulsante_con_nome(self, titolo, on_click):
        pulsante = QPushButton(titolo)
        pulsante.setStyleSheet("background-color: #add8e6; font-size: 15px; font-weight: bold;")
        # pulsante.setFixedWidth(500)
        # pulsante.setFixedHeight(40)
        # pulsante.setStyleSheet("font-size: 24px")
        if titolo == 'Esci':
            pulsante.setStyleSheet("background-color: #66cdaa; font-size: 13px; font-weight: bold;")
            pulsante.setShortcut("Esc")
        pulsante.clicked.connect(on_click)
        return pulsante

    # metodo che restituisce la lista dei clienti iscritti e registrati nella palestra
    def go_gestione_palestra(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.close()
        return self.vista_lista_clienti.show()

    # metodo che restituisce la lista dei dipendenti del centro sportivo
    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.close()
        return self.vista_lista_dipendenti.show()

    # metodo che reindirizza alla finestra di gestione delle prenotazioni
    def go_gestione_campi(self):
        if self.combo_campo.currentIndex()!=0:
            VistaHome.selezione_campo = self.combo_campo.currentText()
            self.cal = Calendario()
            self.close()
            return self.cal.show()

    # metodo che reindirizza alla gestione della cassa
    def go_gestione_cassa(self):
        self.vista_lista_movimenti = VistaListaMovimenti()
        self.close()
        return self.vista_lista_movimenti.show()

    def funz_esci(self):
        from home.login.Login import Login
        self.vista_login = Login()
        self.close()
        return self.vista_login.show()
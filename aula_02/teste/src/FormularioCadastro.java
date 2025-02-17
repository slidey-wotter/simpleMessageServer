// Componentes básicos do Swing
// import javax.swing.*;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JComboBox;
import javax.swing.JCheckBox;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.BorderFactory;
import javax.swing.SwingUtilities;

// Gerenciadores de layout
// import javax.awt.*;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.FlowLayout;

// Classes para tratamento de eventos
// import javax.awt.event.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Classe que demonstra a criação de uma interface gráfica usando Java Swing Tópicos abordados: -
 * Herança de JFrame para criar janelas - Uso de layouts para organização dos componentes -
 * Componentes básicos do Swing - Programação orientada a eventos
 */
public class FormularioCadastro extends JFrame {
    // Declaração dos componentes da interface
    // Os componentes são declarados como atributos para serem acessíveis em toda a classe
    private JTextField txtNome;
    private JTextField txtEmail;
    private JComboBox<String> cbxGenero;
    private JCheckBox chkNewsletter;
    private JButton btnSalvar;
    private JButton btnLimpar;

    public FormularioCadastro() {
        // SEÇÃO 1: Configuração básica da janela
        // Demonstra as propriedades fundamentais de um JFrame
        setTitle("Formulário de Cadastro");
        setSize(400, 300); // Define largura e altura da janela
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Comportamento ao fechar
        setLocationRelativeTo(null); // Centraliza a janela na tela

        // SEÇÃO 2: Gerenciamento de Layout
        // Demonstra o uso de diferentes tipos de layout para organizar componentes
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout(10, 10)); // Layout principal com áreas Norte, Sul,
                                                       // Leste, Oeste e Centro
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10)); // Adiciona margem ao
                                                                              // redor

        // SEÇÃO 3: Organização em Grid
        // Demonstra o uso do GridLayout para organizar componentes em grade
        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(4, 2, 5, 5)); // 4 linhas, 2 colunas, gaps de 5 pixels

        // SEÇÃO 4: Componentes de Interface
        // Demonstra diferentes tipos de componentes do Swing

        // 4.1: Campos de texto (JTextField)
        inputPanel.add(new JLabel("Nome:"));
        txtNome = new JTextField(20);
        inputPanel.add(txtNome);

        inputPanel.add(new JLabel("Email:"));
        txtEmail = new JTextField(20);
        inputPanel.add(txtEmail);

        // 4.2: Componente de seleção (JComboBox)
        inputPanel.add(new JLabel("Gênero:"));
        String[] generos = {"Selecione", "Masculino", "Feminino", "Outro"};
        cbxGenero = new JComboBox<>(generos);
        inputPanel.add(cbxGenero);

        // 4.3: Caixa de seleção (JCheckBox)
        inputPanel.add(new JLabel(""));
        chkNewsletter = new JCheckBox("Receber newsletter");
        inputPanel.add(chkNewsletter);

        // SEÇÃO 5: Layout para Botões
        // Demonstra o uso do FlowLayout para organizar botões
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout(FlowLayout.RIGHT)); // Alinha botões à direita

        btnSalvar = new JButton("Salvar");
        btnLimpar = new JButton("Limpar");

        // SEÇÃO 6: Programação Orientada a Eventos
        // Demonstra o uso de listeners para responder a eventos
        btnSalvar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                salvarDados(); // Método chamado quando o botão é clicado
            }
        });

        btnLimpar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                limparFormulario();
            }
        });

        buttonPanel.add(btnSalvar);
        buttonPanel.add(btnLimpar);

        // SEÇÃO 7: Montagem Final do Layout
        // Demonstra a hierarquia de painéis e componentes
        mainPanel.add(inputPanel, BorderLayout.CENTER);
        mainPanel.add(buttonPanel, BorderLayout.SOUTH);

        add(mainPanel);
    }

    /**
     * Método que demonstra validação básica e processamento de dados do formulário Importante para
     * mostrar como acessar valores dos componentes
     */
    private void salvarDados() {
        // Validação básica dos campos
        if (txtNome.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Por favor, preencha o nome!", "Erro",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        // Validação do campo de email
        if (txtEmail.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Por favor, preencha o email!", "Erro",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        // Demonstração de como coletar dados dos diferentes tipos de componentes
        String mensagem = "Dados cadastrados:\n" + "Nome: " + txtNome.getText() + "\n" + // Obtém
                                                                                         // texto de
                                                                                         // JTextField
                "Email: " + txtEmail.getText() + "\n" + "Gênero: " + cbxGenero.getSelectedItem()
                + "\n" + // Obtém item selecionado do JComboBox
                "Newsletter: " + (chkNewsletter.isSelected() ? "Sim" : "Não"); // Obtém estado do
                                                                               // JCheckBox

        JOptionPane.showMessageDialog(this, mensagem, "Sucesso", JOptionPane.INFORMATION_MESSAGE);
    }

    /**
     * Método que demonstra como manipular o estado dos componentes Importante para mostrar como
     * modificar valores dos componentes
     */
    private void limparFormulario() {
        txtNome.setText(""); // Define texto vazio
        txtEmail.setText("");
        cbxGenero.setSelectedIndex(0); // Seleciona primeiro item
        chkNewsletter.setSelected(false); // Desmarca checkbox
    }

    /**
     * Método main que demonstra a inicialização correta de aplicações Swing Importante usar
     * SwingUtilities.invokeLater para evitar problemas de thread
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new FormularioCadastro().setVisible(true);
            }
        });
    }
}

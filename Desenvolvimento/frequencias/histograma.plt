# Vamos colocar um título descritivo no nosso script
set title ARG3

# Dizemos que os dados estão separados por vírgula no arquivo de dados
set datafile separator ","

# Vamos adicionar um grid para facilitar a divisão dentro do gráfico
set grid

set style data histogram

# Aumenta a largura das barras
set boxwidth 2

# Adicionamos preenchimento de cor dentro das barras
set style fill solid

# Rotaciona os textos no eixo X em 90 graus
set xtic rotate by 0

# Adiciona margem na parte inferior para caber nomes no eixo x
set bmargin 8

# Posiciona os textos na margem inferior
set xtics offset 0.5, 0

# Diminui o tamanho da fonte no eixo x
set xtics font ", 10"

# Dá uma borda maior nas laterais do gráfico
set border 10

# Saída no formato png e de tamanho 800x600
set terminal 'png' size 800,600

set output ARG2

# Arquivo de entrada usando a coluna 2 para dados e a coluna 1 como texto no
# eixo X além de definir o título da legenda desses dados
plot ARG1 using 2:xtic(1) title "Ocorrência no texto"


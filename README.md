# nalot-fotogrametryczny
Aplikacja modelująca nalot fotogrametryczny

# 1. Wstęp

Celem projektu było stworzenie aplikacji pozwalającej na podstawową symulację nalotu
fotogrametrycznego. W projekcie zrealizowano część obliczeniową oraz część graficzną w postaci
wizualizacji nalotu. Nalot polegał na przelocie specjalistycznego samolotu nad mierzonym teren. Do
samolotu przyczepiona była kamera wykonująca zdjęcia terenu w wysokiej rozdzielczości. Po
wykonaniu nalotu, na podstawie zdjęć stworzono ortofotomapę.

# 2. Opis programu

Program zrealizowano w języku programistycznym python. Skorzystano z następujących
bibliotek:

• matplotlib – biblioteka umożliwiająca tworzenie wykresów

• tkinter – biblioteka umożliwiające tworzenie GUI

• customtkinter – biblioteka stworzona na podstawie biblioteki tkinter, dzięki której można stworzyć nowocześnie wyglądające GUI dla aplikacji

Powyższe biblioteki można zainstalować przy pomocy komendy „pip install <nazwa biblioteki>”
wpisanej w terminal projektu. Na projekt składają się dwa pliki:

• main.py – plik zawierający funkcję wykonawczą aplikacji oraz klasę GUI aplikacji

• classes.py – plik zawierający definicje klas Plane oraz Camera

Pliki main.py i classes.py muszą być w jednym folderze. Aby włączyć aplikację należy uruchomić
skrypt pliku main.py.
Program korzysta z dwóch klas – Plane oraz Camera. Obiekty tych klas są następnie
wykorzystywane w obliczeniach, które przeprowadzane są w funkcji calculations() w klasie App.
Następnie wartości zwrócone prze funkcję calculations() są wykorzystywane w funkcji plotPlane() do
rysowania wykresu. Obie funkcje są wywoływane są w funkcji draw(), przypisanej do przycisku.
Dodatkowo w tej funkcji sczytywane są wartości wprowadzone przez użytkownika.
Użytkownik programu może podać własne parametry, oraz wybrać samolot i kamerę.
Użytkownik może wprowadzić tylko wartości całkowite lub zmiennoprzecinkowe(rozdzielone
kropką). Jednostki w jakich mają być wprowadzone dane są podane. Dodatkowo po wykonaniu
obliczeń na konsoli zostanie wypisany całkowity czas lotu uwzględniając trasę z lotniska nad teren,
oraz trasę powrotną na lotnisko.

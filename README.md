# BD2_API
#Chat_GPT_bo_3_w_nocy
Ten projekt to aplikacja Flask zaprojektowana z myślą o separacji trosk, dzieląca swoją strukturę na logikę aplikacji, modele bazy danych oraz warstwy prezentacji. Zawiera również skrypty testowe, aby zapewnić niezawodność i wydajność.

## Struktura

Projekt jest zorganizowany w następujący sposób:

- `application/`: Ten katalog zawiera rdzeń aplikacji Flask.
  - `__init__.py`: Inicjalizuje aplikację Flask i konfiguruje SQLAlchemy do interakcji z bazą danych. Ustawia niezbędne środowisko, aby aplikacja mogła działać płynnie, integrując komponenty i rozszerzenia.
  - `models.py`: Zawiera definicje modeli SQLAlchemy. Te modele reprezentują tabele bazy danych i ich relacje, umożliwiając podejście ORM do zarządzania bazą danych.
  - `views.py`: Definiuje widoki / punkty końcowe Flask. Te funkcje lub klasy są odpowiedzialne za obsługę żądań i zwracanie odpowiedzi do klienta, zasadniczo określając, co jest wyświetlane.
  - `test_connection.py`: Skrypt zaprojektowany do testowania łączności z bazą danych. Zapewnia to, że aplikacja może pomyślnie komunikować się z wyznaczoną bazą danych.
  
- `Tests/`: Zawiera testy jednostkowe aplikacji.
  - `test_get_position.py`: Specyficzny przypadek testowy zaprojektowany do walidacji funkcjonalności związanej z pobieraniem pozycji z bazy danych.

- `app.py`: Punkt wejścia do uruchamiania aplikacji Flask. Ten skrypt korzysta z frameworka Flask, aby uruchomić serwer sieciowy i obsłużyć aplikację.

- `requirements.txt`: Lista wszystkich niezbędnych pakietów Pythona i ich wersji wymaganych do uruchomienia tego projektu. Jest kluczowa dla ustanowienia spójnego środowiska deweloperskiego i produkcyjnego.

## Instalacja

Aby uruchomić ten projekt na swoim lokalnym komputerze, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowanego Pythona.
2. Sklonuj to repozytorium na swoją maszynę lokalną.
3. Zainstaluj zależności:

pip install -r requirements.txt
4. Uruchom aplikację:
python app.py

To uruchomi aplikację Flask na domyślnym porcie, czyniąc ją dostępną przez przeglądarkę internetową.

## Testowanie

Aby uruchomić testy i upewnić się, że wszystko działa zgodnie z oczekiwaniami, przejdź do głównego katalogu projektu i odpal


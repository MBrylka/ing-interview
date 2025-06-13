# Uruchamianie testów:



```
pytest --browser chromium --numprocesses auto --base-url https://www.ing.pl --video on --html report.html --self-contained-html;
```

Parametry

--browser = nazwa przegladarki do uruchominia testow

--numprocesses auto = pozwala na wielowatkowe uruchamianie testow 

--base-url = URL do testow, mozna wykorzystac do uruchamiania tych samych testow na roznych srodowiskach

--video on = zapisuje nagranie z przebiegu testu w folderze videos

--html report.html = przy uzyciu pytest-html generowany jest raport z testu.

--self-contained-html = dodatkowo flaga aby css był osadzony w pliku z raportem.

# Struktura
Uzylem prostego modelu POM:
w folderze pages znajduje sie klasa obslugująca strone główną - LandingPage

Dodatkowo w folderze components dodałem klasę odpowiedzialna za okno z ciasteczkami. umieściłbym tutaj elementy które są niezaleźne od tego na jakiej stronie jestemy jak np. Gorne menu.

Instancja tej klasy zostala umieszczona w klasie LandingPage na zasadzie komponentu. W ten sposob moge dodawac odpowiednie komponenty UI do mojego obiektu POM
w zaleznosci czego bede potrzebowal.


# Uzyte biblioteki:

pytest-html - generowanie raportów html.

pytest-xdist - mozliwosc uzycia kilku wątków


# Infromacje
Uruchamiając test z poziomu githuba naleźy przejść captche. 
Jedyne czego próbowalem do uzycie playwright-stealth ale tez zostalem wykryty. 
Mozna by uzyc tez proxy aby wykrylo to jako uzytkownika z Polski.

Wlaściwym rowziązaniem byloby albo wylaczenie captchy na srodowisku testowym 
albo uzycie API_KEY z captchy aby w latwy sposób ją pominąć



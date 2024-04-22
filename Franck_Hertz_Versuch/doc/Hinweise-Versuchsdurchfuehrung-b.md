# Hinweise für den Versuch Gammaspektroskopie

## Versuchsdurchführung [3/4]

### Aufgabe 2: Charakterisierung der $\mathrm{Hg}$-Röhre

#### Aufgabe 2.1: Bestimmung der Spannungsdifferenz $\Delta U_{B}$ und der effektiven Kontaktspannung $U_{\mathrm{th.}}$

- Einen schematischen Verlauf von $I_{A}$ als Funktion von $U_{B}$ ist in **Abbildung 2** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Franck_Hertz_Versuch/doc/Hinweise-Franck-Hertz.md) gezeigt. Die Differenz $\Delta U_{B}$ lässt sich sowohl aus den Maxima, als auch aus den Minima des Verlaufs bestimmen. Im Versuch sollten Sie bis zu fünf Maxima bestimmen können. 

- Tragen Sie in einem ersten Diagramm D1 zunächst $I_{A}$ gegen $U_{1}+U_{2}$ auf. Die Lage des ersten Maximums der Verteilung $U_{1+2}^{(1)}$ liegt bei einem Wert von $U_{1}+U_{2}$ der größer ist als $\Delta U_{B}$, danach sollten die Lagen aller weiteren Maxima $U_{1+2}^{(i)}$ und $U_{1+2}^{(i+1)}$ den gleichen Abstand $\Delta U_{B}$ zueinander aufweisen. Nach Gleichung **(1)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Franck_Hertz_Versuch/doc/Hinweise-Franck-Hertz.md) entspricht der Differenzbetrag zwischen $U_{1+2}^{(1)}$ und $\Delta U_{B}$ der effektiven Kontaktspannung $U_{\mathrm{th.}}$. Sie können zur gleichzeitigen Bestimmung von $\Delta U_{B}$ und $U_{\mathrm{th.}}$ z.B. wie folgt vorgehen:

  - Bestimmen Sie die Lage, der $N$ Maxima aus Ihrer Messung mit entsprechender Unsicherheit, z.B. aus der Anpassung einer Normalverteilung auf einer geeignet gewählten Untergrundfunktion. 

    Tragen Sie daraufhin in einem zweiten Diagramm D2 die Indizes der Maxima ($i=1\ldots N$) auf der $x$-Achse gegen die Lagen $U_{1+2}^{(i)}$ der $i$ Maxima auf der $y$-Achse auf. An D2 können Sie ein Modell der Form

    ```math
    \begin{equation*}
    U_{B}^{(i)}(\Delta U_{B}, U_{\mathrm{th.}}) = \Delta U_{B}\cdot i + U_{\mathrm{th.}}
    \end{equation*}
    ```

    anpassen, aus dem Sie $\Delta U_{B}$ und $U_{\mathrm{th.}}$ gleichzeitig bestimmen können, ohne Information zur Bestimmung beider Parameter mehr als einmal zu verwenden. Für die Anpassung mit Hilfe eines XYFits aus dem Programmpaket kafe2 können Sie den Indizes auf der $x$-Achse eine sehr kleine Unsicherheit von $10^{-3}$ zuordnen.  

- Kalibrieren Sie für Ihre Auswertung mit Hilfe von $U_{\mathrm{th.}}$ die $x$-Achsen aller weiteren aufgenommenen Diagramme (wo angebracht) entsprechend auf $U_{B}$. 


#### Aufgabe 2.2: Verlauf des Anodenstroms $I_{\mathrm{G2}}$

- Das Schottky-Langmuirschen [Raumladungsgesetz](https://de.wikipedia.org/wiki/Raumladungsgesetz) gilt streng genommen nur für evakuierte Dioden. Die Spannung $U_{3}$ ist für diese Aufgabe irrelevant. Regeln Sie daher sowohl $U_{1}$ als auch $U_{3}$ auf Null. 

- Bestimmen Sie $I_{\mathrm{G2}}$ für eine geeignet hohe Anzahl, mindestens aber für 10 verschiedene Werte von $U_{2}$. Nehmen Sie sowohl für $I_{\mathrm{G2}}$ als auch für $U_{2}$ geeignete Unsicherheiten an.

- Passen Sie an den resultierenden Kurvenverlauf ein Modell der Form

  ```math
  \begin{equation*}
  I_{\mathrm{G2}}(\kappa,\,) = \kappa\,\left(U_{2}+U_{\mathrm{th.}}\right)^{\gamma}
  \end{equation*}
  ```

  an, wobei $\kappa$, $U_{\mathrm{th.}}$ und $\gamma$ freie Parameter der Anpassung sind. 

- Fügen Sie Ihrem Protokoll zusätzlich zu Ihrer Auswertung den auf die Anzahl der Freiheitsgrade normierten $\chi^{2}$-Wert oder den $p$-Wert der Anpassung zu. Innerhalb der resultierenden Unsicherheiten sollte $U_{\mathrm{th.}}$ mit dem aus **Aufgabe 2.1** ermittelten Wert und $\gamma$ mit dem Wert 3/2 übereinstimmen.  

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch/doc/Hinweise-Versuchsdurchfuehrung-a.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch/doc/Hinweise-Versuchsdurchfuehrung-c.md)

# Hinweise für den Versuch: "Spezifische Wärmekapazität" 

## Versuchsdurchführung

### Aufgabe 1: Spezifische Wärmekapazität durch Mischtemperatur

Für Ihre Messungen stehen Ihnen die folgenden weiteren Metalle zu Verfügung:
   * Aluminium (Erwartung $896\, \mathrm{J\,kg^{-1}\,K^{-1}}$);
   * Kupfer (Erwartung $385\, \mathrm{J\,kg^{-1}\,K^{-1}}$); 
   * Messing (Erwartung $376\, \mathrm{J\,kg^{-1}\,K^{-1}}$); 
   * Blei (Erwartung $131\, \mathrm{J\,kg^{-1}\,K^{-1}}$); und 
   * Zinn (Erwartung $221\, \mathrm{J\,kg^{-1}\,K^{-1}}$).

Erwartung jeweils bei  bei $20^{\circ}\mathrm{C}$.

####  Aufgabe 1.1: Planung und Messvorhaben

Wichtige Fragen, die Sie bei der Bearbeitung dieser Aufgabe beantworten sollten sind: 

- Sollten Sie lieber ein kompaktes Metallstück benutzen oder ein Granulat?
- Sollten Sie zur Herstellung der Mischtemperatur heißes Metall und kaltes Wasser verwenden oder umgekehrt? 
- Ist Wasser oder eine andere Flüssigkeit geeigneter? 
- Was sind günstigste Anfangs- bzw. Endtemperaturen für Ihre Messung? 
- Welche Massen (für Wasser und Metall) sollten Sie benutzen und wie und zu welchem Zeitpunkt der Messung sollten Sie diese bestimmen? 
- Sollten Sie Massenfehler durch anhaftendes Wasser oder durch die an das Kalorimeter und Zubehör abgegebene Wärmemenge (Wärmegang) berücksichtigen? 
- Wie wollen Sie den Wärmegang des gesamten Aufbaus abschätzen?
- Wie schaffen Sie es bei Wiederholung der Messung immer wieder wohldefinierte Anfangsbedingungen herzustellen (das Metall erhitzt sich oder kühlt sich ab, das gleiche gilt für das Wasser oder das Kalorimeter)? 
- Sind Ihre Messungen reproduzierbar und die Ergebnisse mit einer statistischen Streuung kompatibel, oder gibt es mögliche Tendenzen (werden die Ergebnisse mit zunehmender Stichprobenlänge z.B. größer oder kleiner)?
- Was ist ein geeignetes Thermometer in Hinblick auf Genauigkeit, Ablesegenauigkeit, oder störende eigene Masse? 
- Genügt Ihnen jeweils eine Temperaturablesung oder sollten Sie die Messung der Temperatur in Abhängigkeit von der Zeit bestimmen?
- Wäre es sinnvoll Hilfsmessungen, mit bekannten Sollergebnissen (z.B. mit Wasser-Wasser-Gemischen) vorzunehmen aus denen Sie die Mischtemperatur vorhersagen können?

Beschreiben und begründen Sie Ihre Versuchsplanung, **messen Sie sorgfältig und dokumentieren Sie Ihr Vorgehen genau.** 

#### Aufgabe 1.2: Durchführung des Messprogramms und Auswertung

- Wiederholen Sie Ihre Messungen mindestens drei–fünf mal zur Abschätzung statistischer Variationen. 
- Variieren Sie das Verfahren in den oben genannten Punkten, um systematische Effekte abzuschätzen. 
- Diskutieren und Beurteilen Sie am Ende der Auswertung das gewählte Verfahren.

### Aufgabe 2: Spezifische Wärmekapazität von Aluminium als Funktion der Temperatur

#### Aufgabe 2.1: Datennahme

- Kühlen Sie den Al-Hohlzylinder (AL) mit Flüssigstickstoff im Nalgene-Isolierbehälter auf $T=-196^{\circ}\mathrm{C}$ (Siedetemperatur von Flüssigstickstoff) ab. 
- Bereiten Sie den Edelstahl-Isolierbehälter (EI) durch Ausschwenken mit Flüssigstickstoff auf die Aufnahme von AL vor. 
- Heizen Sie AL dann mit Hilfe der eingebauten Heizwicklung innerhalb von EI mit konstanter Heizleistung (von $\lesssim 20\,\mathrm{W}$) wieder auf und zeichnen Sie mit Hilfe des Datenloggers den Verlauf der Temperatur als Funktion der Zeit $T(t)$ auf. **Heizen Sie den Zylinder nicht mit einer Stromstärke $I>2\ \mathrm{A}$, da sie sonst Gefahr laufen den Aufbau zu zerstören.** 
- Zu diesem Zweck ist ein $\mathrm{NiCr}$-$\mathrm{Ni}$-Thermoelement (TE) in AL befestigt; mit Hilfe von Eiswasser können Sie TE eine stabile Referenztemperatur von $T_{\mathrm{ref}}=0^{\circ}\mathrm{C}$ zur Verfügung stellen. Sie müssen TE für die Messung von Temperaturen erst noch geeignet kalibrieren, d.h. die von TE ausgegebenen Spannungen in Temperaturen umrechnen (siehe **Aufgabe 2.2**).

- Sie können diese Messung bereits starten, noch bevor Sie mit **Aufgabe 1** beginnen. Sie läuft, abgesehen von gelegentlichen Kontrollen der Heizleistung, automatisch ab. **Behalten Sie Strom und Spannung aber auf jeden Fall im Auge, damit der Aufbau nciht überhitzt wird.** 

#### Aufgabe 2.2: Kalibration des Thermoelements

- Bestimmen Sie durch Anpassung einer geeigneten analytischen Funktion an die Messpunkte der Datei [calibration.csv](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Spezifische_Waermekapazitaet/params/calibration.csv) eine Kalibrationsfunktion $K(U, T)$, um die aufgezeichneten Spannungen $U(t)$ aus Ihrer Messung in Temperaturen $T(t)$ umzurechnen. 
- Schätzen Sie hierzu für jeden Messpunkt geeignete Unsicherheiten $\Delta T$ und $\Delta U$ ab. 
- Stellen Sie die Messpunkte und $K(U, T)$ geeignet dar.
- Fügen Sie Ihrer Auswertung eine Diskussion des $\chi^{2}$-Werts der durchgeführten Anpassung zu.  

#### Aufgabe 2.3: Korrektur des Wärmegangs

- Korrigieren Sie die Daten mit Hilfe von $K(U, T)$ aus **Aufgabe 2.2**. 

- Passen Sie ein Modell z.B. der folgenden Form an: 
  ```math
  \begin{equation*}
  T_{0}(t)=\alpha+\beta\,e^{t/\gamma},
  \end{equation*}
  ```

  wobei $\alpha$, $\beta$ und $\gamma$ freie Parameter des Modells sind. 

- Fügen Sie Ihrer Auswertung eine geeignete Darstellung der Messpunkte, und der Anpassung zu. 

- Fügen Sie Ihrer Auswertung eine Diskussion des $\chi^{2}$-Werts der durchgeführten Anpassung zu.

- Korrigieren Sie für ihre Auswertung die Messung aus **Aufgabe 2.1** um den so ermittelten Verlauf des Wärmegangs.   

#### Aufgabe 2.4: Bestimmung von $c_{\mathrm{Al}}(T)$

- Bestimmen Sie hierzu zunächst durch Anpassung eine analytische Funktion zur Beschreibung des korrigierten Verlaufs von $T(t)$. Hierzu eignet sich ein Modell der Form

  ```math
  \begin{equation}
  T(t) = a\,t^{b} + c,
  \end{equation}
  ```

  mit den freien Parametern $a$, $b$ und $c$. 

- Fügen Sie Ihrer Auswertung eine geeignete Darstellung der Messpunkte und der Anpassung zu. 

- Fügen Sie Ihrer Auswertung eine Diskussion des $\chi^{2}$-Werts der durchgeführten Anpassung zu.

- Aus dem Modell können Sie die Ableitung wie folgt leicht bestimmen: 

  ```math
  \begin{equation*}
  \dot{T}(t) = a\,b\,t^{b-1}.
  \end{equation*}
  ```

- Um $\dot{T}$ als Funktion von $T$ zu bestimmen benötigen Sie noch die Umkehrfunktion von Gleichung **(1)** 

  ```math
  \begin{equation*}
  t(T) = \left(\frac{T-c}{a}\right)^{1/b}.
  \end{equation*}
  ```

- Nach Einsetzen ergibt sich eine analytische Abschätzung des gesuchten Zusammenhangs zu 
  ```math
  \begin{equation*}
  \dot{T}(T) = a\, b\, \left(\frac{T-c}{a}\right)^{\frac{b-1}{b}}.
  \end{equation*}
  ```

- Verwenden Sie Monte Carlo Methode, um die Unsicherheiten $\Delta a$, $\Delta b$ und $\Delta c$ auf den Verlauf von $\dot{T}(T)$ fortzupflanzen, wie [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Spezifische_Waermekapazitaet/tools/heat_capacity.py) gezeigt.

- Fügen Sie Ihrem Protokoll eine geeignete Darstellung des Verlaufs mit entsprechendem Fehlerband zu. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Spezifische_Waermekapazitaet)

 


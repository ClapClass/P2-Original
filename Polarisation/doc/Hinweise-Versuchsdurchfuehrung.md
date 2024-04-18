# Hinweise für den Versuch Photoeffekt

## Versuchsdurchführung

### Aufgabe 1: Polarisiertes Licht aus dem Wasserglas

- Beobachten Sie das Streulicht durch einen Polarisationfilter von der Seite und von oben. 

### Aufgabe 2: Erzeugung und Untersuchung von Licht mit verschiedener Polarisation

#### Aufgabe 2.1: Aufbau des Strahlengangs

- Überlegen Sie sich ein möglichst günstiges optisches System zur Erzeugung und Untersuchung verschieden polarisierten Lichts. Hierzu stehen Ihnen die Polarisationsfilter PF und AF, eine Linse, zur Fokussierung des Strahls, ein Farbfilter und mehrere drehbar montierte VP zur Verfügung. 
- Achten Sie beim Strahlengang darauf, dass sich die Mitten der optischen Elemente auf der Strahlachse und die Ebenen der optischen Elemente senkrecht zu dieser befinden.
- Die Intensität des Lichts bestimmen Sie mit Hilfe der durch PZ angezeigten Spannung $U$. Nehmen Sie für jede Messung 36 Messpunkte, jeweils in Schritten von $5^{\circ}$ zwischen $\varphi=0\ldots180^{\circ}$ auf. 
- Tragen Sie die Messpunkte linear auf und passen Sie an alle Messreihen eine geeignete Sinus-/Cosinus-Funktion an. Schätzen Sie hierzu geeignete Unsicherheiten $\Delta\varphi$ und $\Delta U$ ab.
- Sie können zusätzlich jeweils auch eine Auftragung in Polarkoordinaten vornehmen. 

##### Untersuchungen zur linearen Polarisation

- Führen Sie Ihre Untersuchungen zur linearen Polarisation **sowohl mit weißem, als auch mit monochromatischem Licht** durch. Das monochromatische Licht können Sie mit dem zur Verfügung stehenden Farbfilter herstellen.

##### Untersuchungen zur elliptischen/zirkularen Polarisation

- Führen Sie Ihre Untersuchungen zur elliptischen/zirkularen Polarisation **nur mit monochromatischem Licht** durch. 

- Im Glimmer, als doppelbrechendem Medium, gibt es zwei optische Achsen entlang derer sich das Licht unterschiedlich schnell ausbreitet (eine "langsame" und eine "schnelle" Achse). Um maximale elliptsche/zirkulare Polarisation zu beobachten müssen Sie die VP im Strahlengang so ausrichten, dass die Lichtintensität entlang beider Achsen gleichgroß ist. Sie erreichen dies z.B. wie folgt: 
  - Polarisieren Sie das Licht linear mit Hilfe von PF.
  - Verdrehen Sie AF, so dass $U=0$.
  - Bringen Sie VP ein, bei zufälliger Ausrichtung sollten Sie $U\neq0$ beobachten.
  - Drehen Sie VP, um wieder den Zustand $U=0$ herzustellen. In diesem Fall verläuft der linear polarisierte Strahl exakt zu einer der Achsen, so dass es bei der Transmission des Lichts nicht zur Änderung der Polarisation kommt. 
  - Verdrehen Sie jetzt AF um $45^{\circ}$, damit sollten Sie erreichen, dass beide optische Achsen des Kristalls mit gleicher Intensität bestrahlt werden. 
  
- Dieses Verfahren müssen Sie für jedes VP immer wieder neu durchführen. 

- Nehmen Sie die Untersuchungen für zwei beliebige VP unterschiedlicher Dicke vor. 

- Gehen Sie dann analog für ein $\lambda/4$-Plättchen vor, dessen Abmessungen so sind, dass Sie zirkular polarisiertes Licht erhalten. 

- Verwenden Sie auch zur Anpassung an die Messreihe zur Untersuchung der zirkularen Polarisation ein Modell, dass eine Anisotropie der Verteilung erlaubt. Bestimmen Sie diese Anisotropie numerisch und diskutieren Sie ggf. ihr Zustandekommen. Eine Möglichkeit dies zu tun sieht z.B. wie folgt aus: 

  - Für perfekt zirkular polarisiertes Licht erwarten Sie eine isotrope Verteilung für $U\neq U(\varphi)$. In der Praxis kann es sein, dass Sie immer noch eine leicht (sinusförmige) Modulation $U(\varphi)$ feststellen. 

  - Sie können diese Modulation quantifizieren, wenn Sie an die Messreihe ein Modell der Form

    ```math
    \begin{equation*}
    U(\varphi) = U_{0}+U_{A}\sin(\Omega\,\varphi+\phi_{0})
    \end{equation*}
    ```

    anpassen, wobei $U_{0}$, $U_{A}$, $\Omega$ und $\phi_{0}$ freie Parameter des Modells sind. Bei einer solchen Anpassung interessieren Sie sich in erster Linie für den Parameter $U_{A}$. Die anderen Parameter dienen dazu die wesentlichen Eigenschaften der Messreihe wiederzugeben. 

  - Überprüfen Sie den $\chi^{2}$-Wert der Anpassung. Weist dieser darauf hin, dass das Modell die Daten gut beschreiben kann überprüfen Sie, wie weit der Wert von $U_{A}$ im Rahmen der aus der Anpassung bestimmten Unsicherheit $\Delta U_{A}$ von 0 entfernt ist (den sog. *pull* $\delta$, siehe z.B. Seite 37/58 [hier](https://labs.physik.kit.edu/downloads/P1Datnauswertung-2023-10-26.pdf)). Für $`\delta>3`$ sprechen wir in der (Teilchen-)physik von einer Evidenz (d.h. von einem Hinweis) auf einen Effekt. Für $`\delta>5`$ von der Beobachtung eines Effekts.

  - Abschließend können Sie eine "Anpassung eines trivialen Modells" mit nur einer Konstanten $U_{0}$ (ohne den zusätzlichen Sinus-Term) durchführen und den $\chi^{2}$-Wert dieser Anpassung überprüfen. Weist dieser wiederum darauf hin, dass dieses triviale Modell die Daten gut beschreiben kann ist eine Anisotropie nicht statistisch nachweisbar.  


#### Aufgabe 2.2: Differenz der Brechungsindizes der beobachteten Strahlen

- Berechnen Sie $\Delta n=\left(n_{\beta} - n_{\gamma}\right)$ aus den in **Aufgabe 2.1** aufgenommenen Intensitätsverteilungen zur elliptischen Polarisation. 

- Den Phasenunterschied $\Delta\phi$ der beiden senkrecht zueinander stehenden Strahlen an der Austrittsfläche von VP können Sie aus dem Verhältnis der maximalen ($\propto U_{\mathrm{max}}$) und minimalen ($\propto U_{\mathrm{min}}$) Intensitäten des elliptisch polarisierten Lichts bestimmen. 

- Das notwendige **Verhältnis der Amplituden** der Strahlen ergibt sich aus der Quadratwurzel des Verhältnisses der Intensitäten. 

- Schließlich erhalten Sie die Phasendifferenz aus dem $\arctan(\ \cdot\ )$ dieses Verhältnisses. 

- Zusammenfassend ergibt sich die Formel: 
  ```math
  \begin{equation*}
  \Delta n = \frac{\lambda_{0}}{2\pi\,d}\arctan\left(\sqrt{\frac{U_{\mathrm{min}}}{U_{\mathrm{max}}}}\right),
  \end{equation*}
  ```

  wobei $d$ der Dicke von VP und $\lambda_{0}$ der Wellenlänge des Lichts im Vakuum entsprechen. Verwenden Sie geeignete Unsicherheiten $\Delta U_{\mathrm{min}}$, $\Delta U_{\mathrm{max}}$ (jeweils aus vorherigen Anpassungen), $\Delta d$ und $\Delta \lambda_{0}$. 

- Bestimmen Sie $\Delta n$ aus beiden ihnen zur Verfügung stehenden Messreihen (für die jeweils unterschiedlichen Dicken $d_{i}$) aus **Aufgabe 2.1** und vergleichen Sie die Ergebnisse.

### Aufgabe 3: Beobachtungen mit polarisiertem Licht

- Diese Aufgaben sind qualitativer Natur. Beschreiben Sie jeweils, was Sie beobachten und fügen Sie Ihrer Auswertung ggf. Photographien zu. Ein Beispiel, wie Sie Photographien direkt in Ihr Jupyter-notebook einfügen können finden Sie [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/tools/add_figures.ipynb). 
- Entfernen Sie für diese Aufgaben den Farbfilter aus dem Strahlengang, bestrahlen Sie die entsprechenden Objekte mit weißem, linear polarisiertem Licht (hinter PF) und beobachten Sie die durchstrahlten Objekte durch AF. 
- Drehen Sie AF und beschreiben Sie, was Sie beobachten.  
- Projizieren Sie hierzu das entstehende Bild an die Wand. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Polarisation)

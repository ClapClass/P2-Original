# Hinweise für den Versuch Vakuum

## Vakuumbereiche

Die Physik des Vakuums ist die [Strömungsmechanik](https://de.wikipedia.org/wiki/Str%C3%B6mungsmechanik). Grundsätzlich unterscheidet man drei Vakuumbereiche, in denen drei Strömungsarten dominant vorherrschen: 

### Grobvakuum ($\gt 1\ \mathrm{mbar}$)

Hier liegt viskose oder [Kontinuumsströmung](https://de.wikipedia.org/wiki/Kontinuumsstr%C3%B6mung) vor, d.h. es dominiert die Wechselwirkungen der Teilchen des Gases (Fluids) untereinander, die die innere Reibung ([Viskosität](https://de.wikipedia.org/wiki/Viskosit%C3%A4t)) des Fluids bestimmen. Treten Wirbel in der Strömung auf, spricht man von [turbulenter Strömung](https://de.wikipedia.org/wiki/Turbulente_Str%C3%B6mung), findet ein Gleiten verschiedener Schichten des Fluids gegeneinander statt, spricht man von [laminarer Strömung](https://de.wikipedia.org/wiki/Laminare_Str%C3%B6mung). 

Viskose Strömung liegt generell dann vor, wenn die [mittlere freie Weglänge](https://de.wikipedia.org/wiki/Mittlere_freie_Wegl%C3%A4nge) $\lambda$ der Teilchen sehr viel kleiner als der Durchmesser der Leitung ist. Die Bewegungsrichtung der Teilchen im Fluid entspricht in diesem Fall der makroskopischen Bewegungsrichtung des Fluids.

### Hoch- ($\lt 10^{-3}\ \mathrm{mbar}$) und Ultrahochvakuum ($\lt 10^{-8}\ \mathrm{mbar}$) 

Hier liegt [molekulare Strömung](https://de.wikipedia.org/wiki/Molekulare_Str%C3%B6mung) vor, in der sich die Teilchen des Fluids ohne gegenseitige Behinderung frei bewegen können. Die Wahrscheinlichkeit eines Teilchen mit den Begrenzungen der Leitung zu stoßen ist deutlich höher, als die Wahrscheinlichkeit der Teilchen untereinander zu stoßen. In diesem Fall ist $\lambda$ sehr viel größer als der Durchmesser der Leitung. Da sie so geringen Einfluss aufeinander haben kann man dem Strom der Teilchen des Fluids keine eindeutige Richtung mehr zuordnen. In diesem Druckbereich hängen viele charakteristische Eigenschaften von Leitungen nicht mehr vom Druck, sondern v.a. von der Oberfläche der Leitungen ab. Teilchen des Fluids können von den Begrenzungen der Leitung absorbiert und nach langen Zeiträumen erst wieder abgegeben werden.

### Feinvakuum ($10^{-3}$ bis $1\ \mathrm{mbar}$) 

Hier liegt der Übergang zwischen Kontinuumsströmung und molekularer Strömung, die sog. [Knudsenströmung](https://de.wikipedia.org/wiki/Knudsenstr%C3%B6mung) vor.

## Viskosität

Um die innere Reibung einer viskosen Strömung zu verstehen betrachten wir den Fall zweier übereinander liegender Flächen in einem Fluid, wie in **Abbildung 1** dargestellt: 

<img src="../figures/Viskositaet.png" width="1000" style="zoom:100%;"/>

**Abbildung 1**: (Übereinandergleitende Schichten eines viskosen Fluids)

---

Wir stellen uns vor, dass sich die graue Fläche $A$ über dem Fluid mit der konstanten Geschwindigkeit $v(z)$ bewegt. Die weiße Grundfläche bei $z=0$ hat die Geschwindigkeit 0. Aufgrund der inneren Reibung der Flüssigkeit erfordert es die Kraft $F$, um die obere Fläche, die andernfalls zum Stillstand kommen würde, mit konstanter Geschwindigkeit fort zu bewegen. Im Kräftegleichgewicht wirkt $F$ die Kraft $F_{R}$ entgegen. In der Modellvorstellung führt die Bewegung mit $v(z)$ zu einer Scherung der übereinander gleitenden Fluidschichten. Die Kraft $F_{R}$ ist proportional zu $A$ und zum Differenzialquotienten $\mathrm{d}v/\mathrm{d}z$ 
$$
\begin{equation}
F_{R}=-\eta\,A\frac{\mathrm{d}v}{\mathrm{d}z}.
\end{equation}
$$
Den Proportionalitätsfaktor $\eta$ bezeichnet man als **Viskosität** des Fluids. Diese Beziehung gilt auch für turbulente Strömungen, die für infinitesimal kleine Volumenelemente immer noch nähergunsweise als laminar angenommen werden können.  

## Gesetz von Hagen-Poiseuille

Für ein zylindrisches Volumenelement mit Abmessungen, wie in **Abbildung 2** gezeigt

<img src="../figures/Hagen-Poiseuille.png" width="1000" style="zoom:100%;"/>

**Abbildung 2**: (Dimensionen eines zylindrischen Volumenelements zur Herleitung des Gesetzes von Hagen-Poiseuille)

---

nimmt Gleichung **(1)** die Form 
$$
\begin{equation*}
F_{R} = -\eta\,2\pi\,r\,\mathrm{dx}\frac{\mathrm{d}v}{\mathrm{d}r}
\end{equation*}
$$
an. Die Bewegung des Fluids durch ein solches Volumenelement kommt durch eine Druckdifferenz 
$$
\begin{equation*}
F=\pi\,r^{2}\bigl(p(x+\mathrm{d}x)-p(x)\bigr) = \pi\,r^{2}\,\mathrm{d}p
\end{equation*}
$$
zustande. Im stationären Fall gilt:
$$
\begin{equation*}
\begin{split}
&F+F_{R}=0;\\
&\\
&\frac{\mathrm{d}v}{\mathrm{d}r} = \frac{r}{2\,\eta}\frac{\mathrm{d}p}{\mathrm{d}x}.
\end{split}
\end{equation*}
$$
Grundbegriffe der Vakuumtechnik
In der Vakuuumtechnik bezeichnet man den Volumendurchfluss (Volumenstrom, siehe Gleichung (3), für viskose Fluide)

V˙≡S
durch die Ansaugöffnung einer Pumpe als Saugvermögen. Je nach Druck und Temperatur (T) verändert sich die Stoffmenge (n) des geförderten Gases bei gleichem Volumendurchfluss.

Die Menge eines Gases kann durch seine Masse m abgeschätzt werden. Bei Gasen gebräuchlicher ist jedoch die Angabe durch das Produkt pV, das nach der idealen Gasgleichung 

pV=nRT=mMmRT;m=pVRTMm,
bei bekannter Temperatur zur Massenangabe äquivalent ist. Dabei entspricht Mm der molaren Masse der Gasmoleküle. Für eine Pumpe ist neben dem Volumen- der Massenfluss

m˙≡qm
von Relevanz, der entsprechend auch als pV-Durchfluss (oder Gasmenge)

qpV=d(pV)dt
angegeben wird. 

Die Saugleistung einer Pumpe wird (in Einheiten einer Leistung) durch qpV an der Ansaugöffnung der Pumpe angegeben. Bei konstantem Druck gilt der einfache Zusammenhang 

qpV=d(pV)dt|p=const.=pV˙=pS
(siehe Gleichung (4) für viskose Fluide). 

Wenn wir beim Saugvorgang von einer adiabatischen Zustandsänderung des Gases (δQ=0) ausgehen erhalten wir: 

δQ=d(pV)=0;=pdV+Vdp=pSdt+Vdp;dpp=−SVdt,
wobei V dem Volumen der evakuierten Apparatur entspricht. Für eine Pumpe, die ein Gas aus einer Apparatur hinreichend großen Volumens V, ohne weiteren Wärmeaustausch absaugt, erwartet man also einen exponentiellen Verlauf des Drucks 

(5)ln⁡(pp0)=−SV(t−t0)p(t)=p0exp⁡(−SV(t−t0)),
wobei p0 dem Anfangs- (z.B. Umgebungs-)druck zum Zeitpunkt t0 zu Beginn des Pumpvorgangs entspricht. 

Strömungsleitwert und -widerstand
Den Proportionalitätsfaktor 

(6)L=πR4p―8ηℓ
in Gleichung (4) bezeichnet man als Strömungsleitwert. Der Kehrwert von L wird als Strömungswiderstand bezeichnet. Beide lassen sich über den Zusammenhang 

qpV∝Δp
allgemein definieren. Gleichung (6) gilt nur für viskose Fluide, für molekulare Strömungen ergibt sich der Zusammenhang: 

(7)L=πkBT18MmR38ℓ,
wobei kB der Boltzmann-Konstanten und T der Temperatur (in K) entsprechen. Der Leitwert wird also vom Druck unabhängig und R geht nur noch in dritter Potenz ein.  

Bei Parallelschaltung von Rohren addieren sich die Saugleistungen, während der Druckunterschied gleich bleibt: 

qpV(ges)=LgesΔp=qpV(1)+qpV(2)=L1Δp+L2Δp=(L1+L2)Δp;Lges=L1+L2.
Bei Serienschaltung von Rohren addieren sich die Druckunterschiede während die Saugleistung gleich bleibt: 

Δpges=Δp1+Δp2;qpVLges=qpVL1+qpVL2;1Lges=1L1+1L2.
Es handelt sich dabei um ein Analogon zu den Kirchhoffschen Regeln der Elektrizitätslehre mit den folgenden Ersetzungen: 

dpdxV˙⟷Idpdx⟷UdpdxL⟷σdpdxL−1⟷R.
Effektive Saugleistung
Eine Pumpe schließt nur selten direkt an die zu evakuierende Apparatur an. Ist dies nicht der Fall, ist das Saugvermögen der Pumpe durch den Gesamtleitwert der verbindenden Leitungselemente reduziert. 

Nimmt man an, dass sich die Temperatur des Gases während des Durchflusses durch die Leitungselemente nicht wesentlich ändert, so dass also der pV-Durchfluss durch die Leitungselemente konstant ist, so erhält man für das effektive Saugvermögen Seff hinter den Leitungselementen den Zusammenhang 

qpV=p1S=p2Seff;Seff=p1p2S.
Für Seff folgt also:

L=qpVp2−p1=p1p2−p1S=p2p2−p1Seff;p2p1=SL+1;SeffL=(1−p1p2)=(1−LS+L)=SS+L;(S+L)Seff=SL;S+LSL=1Seff1L+1S=1SeffSeff=(1L+1S)−1.
Die effektive Saugleistung der Pumpe ergibt sich also durch "Serienschaltung" mit den entsprechenden Leitungselementen.Für den Fluss eines Fluids durch ein zylindrisches Rohr mit Radius $R$ wählen wir die Randbedingung $v(R)=0$. Integriert man mit diesen Randbedingungen den obigen Ausdruck von $R$ bis $r$ erhält man das Geschwindigkeitsprofil des Fluids
$$
\begin{equation}
v(r) = \int\limits_{R}^{r}\frac{r}{2\,\eta}\,\frac{\mathrm{d}p}{\mathrm{d}x}\,\mathrm{d}r = \frac{r^{2}-R^{2}}{4\,\eta}\frac{\mathrm{d}p}{\mathrm{d}x},
\end{equation}
$$
das eine $r^{2}$-Abhängigkeit aufweist. Eine laminare Strömung in kreiszylindrischen Rohren mit einer solchen Geschwindigkeitsverteilung nennt man [Poiseuille’sche Strömung](https://de.wikipedia.org/wiki/Gesetz_von_Hagen-Poiseuille). Integriert man das Geschwindigkeitsprofil aus Gleichung **(2)** zusätzlich über die Querschnittsfläche des Rohrs (in der $yz$-Ebene in **Abbildung 2**) erhält man den **Volumendurchfluss** durch das Rohr:
$$
\begin{equation}
\dot{V} = \int\limits_{0}^{2\pi}\int\limits_{0}^{R}\frac{r^{2}-R^{2}}{4\,\eta}\frac{\mathrm{d}p}{\mathrm{d}x}\,r\,\mathrm{d}\varphi\,\mathrm{d}r = -\frac{\pi\,R^{4}}{8\,\eta}\,\frac{\mathrm{d}p}{\mathrm{d}x}.
\end{equation}
$$
Das Minuszeichen in Gleichung **(3)** zeigt, dass $\dot{V}$ der Druckdifferenz entgegen gerichtet ist, d.h. "das Fluid fließt in Richtung des geringeren Drucks". Gleichung **(3)** bezeichnet man als das **Gesetzt von Hagen-Poisseuille**. Demnach gilt entlang der Stömungsrichtung $x$: 
$$
\begin{equation*}
\dot{V}\propto R^{4};\qquad \dot{V}\propto \frac{\mathrm{d}p}{\mathrm{d}x}.
\end{equation*}
$$
Für strömdende Gase ist zwar der Massenfluss $\dot{m}$, nicht aber $\dot{V}$ konstant. Trotzdem ist Gleichung **(3)** differenziell anwendbar. Man verwendet es in diesem Fall oft in der Form
$$
\begin{equation}
\begin{split}
& p\dot{V}\,\mathrm{d}x = -\frac{\pi\,R^{4}}{8\,\eta}\,p\,\mathrm{d}p; \\
&\\
&\text{Nach Separation der Variablen:}\\
&\\
&\int\limits_{0}^{\ell}p\dot{V}\,\mathrm{d}x = -\int\limits_{p_{\mathrm{ein}}}^{p_{\mathrm{aus}}}\frac{\pi\,R^{4}}{8\,\eta}\,p\,\mathrm{d}p; \\
&\\
&p\,\dot{V} = -\frac{\pi\,R^{4}}{8\,\eta\,\ell}\left(\frac{p_{\mathrm{aus}}^{2}}{2}-\frac{p_{\mathrm{ein}}^{2}}{2}\right) = 
-\frac{\pi\,R^{4}}{8\,\eta\,\ell}\,\overline{p}\,\Delta p \\
&\\
&\text{mit:} \\
&\\
&\overline{p} = \frac{p_{\mathrm{aus}}+p_{\mathrm{ein}}}{2}; \qquad \Delta p = p_{\mathrm{aus}}-p_{\mathrm{ein}},
\end{split}
\end{equation}
$$

wobei $\ell$ dem Abstand zwischen den Messpunkten von $p_{\mathrm{ein}}$ und $p_{\mathrm{aus}}$ entspricht. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Vakuum) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum-a.md)




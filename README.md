# E2E fördjupning
## Vecka 41

<br>

### Status uppgifter

| Uppgift                   | Status | 🟠🟡🟢 |
|---------------------------|--------|--------|
| 1 - Gruppövning           | 100%   | 🟢     |
| 2 - Öva mera              | 100%   | 🟢     |

### 1 - Gruppövning

1. Betrakta https://lejonmanen.github.io/timer-vue/.<br> Skriv user stories som beskriver vad användaren ska kunna göra:

#### User Stories:
<pre>
Som x
vill jag kunna skapa och ta bort widgets
så att sidan blir anpassad efter hur jag vill ha den
</pre>
<pre>
Som x
vill jag byta plats på två widgets
så att sidan blir anpassad efter hur jag vill ha den
</pre>
<pre>
Som x
vill jag ändra tidsinställning på timer
så att den motsvarar min paus
</pre>
<pre>
Som x
vill jag kunna starta, pausa och återställa tiden
så att jag kan anpassa tiden enligt mina val
</pre>
<pre>
Som x
vill jag kunna ändra texten i min anteckning
för att få den text jag vill
</pre>
<pre>
Som x
vill jag kunna ändra temafärg
så att jag kan ha den färg jag tycker mest om
</pre>


2. Formulera acceptanskriterier för alla user stories.

#### Acceptanskriterier:

<pre>
AK1: När jag lägger till en widget så ska den vara synlig på webbsidan.
</pre>
<pre>
AK2: När jag har lagt till en timer och en anteckning
så vill jag byta plats på dom så att anteckningen ligger ovanför timern.
</pre>
<pre>
AK3: När jag ändrar tid och trycker på reset ska den nya tiden visas på timern.
</pre>
<pre>
AK4.1 När jag trycker på Start så ska tiden börja ticka ner.
AK4.2 När jag trycker på Paus ska tiden stanna.
AK4.3 När jag trycker på Reset ska tiden återställas till den fördefinierade tiden.
</pre>
<pre>
AK5: När jag ändrar texten i min anteckning och trycker enter så ska min text visas på sidan.
</pre>
<pre>
AK6: När jag trycker på en temafärg så ska färgen på sidan ändras till motsvarande tema.
</pre>


3. Skriv ner testscenarier för varje acceptanskriterium.<br>(Ett scenario kan täcka in flera acceptanskriterier.)


4. Implementera E2E-tester i Playwright för utvalda scenarier.<br>Gör så många ni hinner med.


### 2 - Öva mera

Utgå från detta formulär: https://tap-ht24-testverktyg.github.io/form-demo/ 
Ta fram user stories, acceptanskriterier, testscenarier och implementera dem i Playwright.

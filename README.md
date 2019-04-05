# Extract infoboxes from wikidumps

To create a wikidump for a specific category or group of articles, you can use [Wikipedia's special export feature](https://en.wikipedia.org/wiki/Special%3aExport).

Download the .xml file and then you can convert the xml dump to a .js file containing a list of infobox objects.

## Installation
```
$ pip3 install wikidump-infobox-extractor
```

## Usage
```
$ infodump <xml dump file path> <output file path>
```

## Example
### xml input:
```
<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="en">
  <siteinfo>
    // ...
  </siteinfo>
  <page>
    <title>Younger v. Harris</title>
    <ns>0</ns>
    <id>1712852</id>
    <revision>
      <id>881592324</id>
      <parentid>877923066</parentid>
      <timestamp>2019-02-03T16:14:22Z</timestamp>
      <contributor>
        <username>Legalskeptic</username>
        <id>11540368</id>
      </contributor>
      <comment>added link to district court opinion</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve" bytes="6017">{{Infobox SCOTUS case
  |Litigants=Younger v. Harris
  |ArgueDate=April 1
  |ArgueYear=1969
  |ReargueDate=April 29
  |ReargueYear=1970
  |ReargueDate2=November 16
  |ReargueYear2=1970
  |DecideDate=February 23
  |DecideYear=1971
  |FullName=Evelle J. Younger, District Attorney of Los Angeles County v. John Harris, Jr., Jim Dan, Diane Hirsch, and Farrel Broslawsky
  |USVol=401
  |USPage=37
  |ParallelCitations=91 S. Ct. 746; 27 [[L. Ed. 2d]] 669; 1971 [[U.S. LEXIS]] 136
  |Prior=Judgment for plaintiffs, 281 [[F. Supp.]] [https://law.justia.com/cases/federal/district-courts/FSupp/281/507/1575355/ 507] ([[United States District Court for the Central District of California|C.D. Cal.]] 1968)
  |Subsequent=
  |Holding=The possible unconstitutionality of a state statute is not grounds for a federal court to enjoin state court criminal proceedings brought pursuant to that statute.  District Court for the Central District of California reversed and remanded.
  |SCOTUS=1970-1971
  |Majority=Black
  |JoinMajority=Burger, Harlan, Stewart, Blackmun
  |Concurrence=Stewart
  |JoinConcurrence=Harlan
  |Concurrence2=Brennan
  |JoinConcurrence2=White, Marshall
  |Dissent=Douglas
  |LawsApplied={{UnitedStatesCode|28|2283}}
}}
'''''Younger v. Harris''''', 401 U.S. 37 (1971),{{ref|citation}} was a case in which the [[United States Supreme Court]] held that [[United States federal courts]] were required to [[abstention doctrine|abstain]] from hearing any [[civil rights]] [[tort]] claims brought by a person who is currently being [[prosecution|prosecuted]] for a matter arising from that claim.

==Facts==
A [[California]] statute prohibited advocating "unlawful acts of force or violence [to] effect political change."  The [[defendant]], Harris, was charged with violating the statute, and he sued under [[42 U.S.C. § 1983]] to get an injunction preventing District Attorney [[Evelle J. Younger]] from enforcing the law on the grounds that it violated the free speech guarantee.

==Decision and precedent==
In an 8-1 decision, the Court held that federal courts may not hear the case until the person is [[convicted]] or found not guilty of the crime unless the defendant will suffer an irreparable injury that is "both great and immediate." Merely having to endure a criminal prosecution is no such irreparable harm.

There are three exceptions to Younger abstention:
#Where the prosecution is in bad faith (i.e. the state knows the person to be innocent)—as applied in ''[[Dombrowski v. Pfister]]''; or
#Where the prosecution is part of some pattern of harassment against an individual; or
#Where the law being enforced is utterly and irredeemably unconstitutional (e.g., if the state were to pass a law making it a crime to say anything negative about its governor under any circumstances).

==Status as precedent==
The doctrine was later extended to situations where the state is seeking to execute a [[civil fine]] against someone, or has jailed a person for [[contempt of court]]. The doctrine applies even where the state does not bring an action until after the person has filed a lawsuit in federal court, provided that the federal court has not yet taken any action on the suit. Moreover, the principle of abstention applies to some state administrative proceedings.

In regard to the exceptions which the ''Younger'' Court articulated, later decisions make it clear that these are highly difficult to meet.
#''Bad faith prosecution'': in no case since ''Younger'' was decided has the Supreme Court found there to exist bad faith prosecution sufficient to justify a federal court injunction against state court proceedings. The Court has specifically declined to find bad faith prosecution even in circumstances where repeated prosecutions had occurred. As commentator [[Erwin Chemerinsky]] states, the bad-faith prosecution exception seems narrowly limited to facts like those in ''Dombrowski''.&lt;ref&gt;Erwin Chemerinsky, ''Federal Jurisdiction'' (5th ed. 2007), Aspen Publishers, p.860&lt;/ref&gt;   Other scholars have even asserted that the possible range of cases which would fit the ''Dombrowski'' model and allow an exception to the no-injunction rule is so limited as to be an "empty universe."&lt;ref&gt;Chemerinsky, p. 859-60&lt;/ref&gt;
#''Patently unconstitutional law'': in no case since ''Younger'' was decided has the Supreme court found there to exist a patently unconstitutional law sufficient to justify a federal court injunction against state court proceedings. The Court has specifically declined to find such patent unconstitutionality in at least one case (Trainor v. Hernandez) &lt;ref&gt;431 US 434 (1977), [https://www.oyez.org/cases/1970-1979/1976/1976_75_1407/ oyez.org]&lt;/ref&gt;
#''Inadequate state forum'': the Supreme Court has found the state forum in question to be inadequate on a small number of occasions.&lt;ref&gt;e.g. Gerstein v. Pugh, 420 U.S. 103 (1975), [https://www.oyez.org/cases/1970-1979/1973/1973_73_477/ oyez.org]
Gibson v. Berryhill, 411 U.S. 564 (1973), [https://www.oyez.org/cases/1970-1979/1972/1972_71_653/ oyez.org]&lt;/ref&gt;

== See also ==
* [[Abstention doctrine]]
* [[Anti-Injunction Act (1793)]]

==References==
{{reflist}}

==External links==
* {{wikisource-inline|Younger v. Harris}}
* {{note|citation}}{{caselaw source
 | case = ''Younger v. Harris'', {{ussc|401|37|1971|el=no}}
 | courtlistener =https://www.courtlistener.com/opinion/108263/younger-v-harris/
 | findlaw = https://caselaw.findlaw.com/us-supreme-court/401/37.html
 | justia =https://supreme.justia.com/cases/federal/us/401/37/
 | oyez =https://www.oyez.org/cases/1970/2
 | loc =http://cdn.loc.gov/service/ll/usrep/usrep401/usrep401037/usrep401037.pdf
 | googlescholar = https://scholar.google.com/scholar_case?case=2453423928277325927
 }}

[[Category:United States Supreme Court cases]]
[[Category:United States Supreme Court cases of the Burger Court]]
[[Category:United States Constitution Article Three case law]]
[[Category:United States abstention case law]]
[[Category:1971 in United States case law]]</text>
      <sha1>rw2jnxxjqezqnunfqwnga1xgjheawtt</sha1>
    </revision>
  </page>
  // ...
```

## Output
```
[{
    "title": "Younger v. Harris",
    "Litigants": "Younger v. Harris",
    "ArgueDate": "April 1",
    "ArgueYear": "1969",
    "ReargueDate": "April 29",
    "ReargueYear": "1970",
    "ReargueDate2": "November 16",
    "ReargueYear2": "1970",
    "DecideDate": "February 23",
    "DecideYear": "1971",
    "FullName": "Evelle J. Younger, District Attorney of Los Angeles County v. John Harris, Jr., Jim Dan, Diane Hirsch, and Farrel Broslawsky",
    "USVol": "401",
    "USPage": "37",
    "ParallelCitations": "91 S. Ct. 746; 27 [[L. Ed. 2d]] 669; 1971 [[U.S. LEXIS]] 136",
    "Prior": "Judgment for plaintiffs, 281 [[F. Supp.]] [https://law.justia.com/cases/federal/district-courts/FSupp/281/507/1575355/ 507] ([[United States District Court for the Central District of California|C.D. Cal.]] 1968)",
    "Subsequent": "",
    "Holding": "The possible unconstitutionality of a state statute is not grounds for a federal court to enjoin state court criminal proceedings brought pursuant to that statute.  District Court for the Central District of California reversed and remanded.",
    "SCOTUS": "1970-1971",
    "Majority": "Black",
    "JoinMajority": "Burger, Harlan, Stewart, Blackmun",
    "Concurrence": "Stewart",
    "JoinConcurrence": "Harlan",
    "Concurrence2": "Brennan",
    "JoinConcurrence2": "White, Marshall",
    "Dissent": "Douglas",
    "LawsApplied": "{{UnitedStatesCode|28|2283}}"
},
// ...
]
```

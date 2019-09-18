# monitoring

<h1>Exhaust Monitoring System</h1>

<center><h2>Abstract</h2></center>
One of the California Air Resources Board’s (CARB) objectives is to transition ocean-going vessel emissions to near-zero with clean, low carbon renewable fuels everywhere to meet air quality and climate goals. The purpose of this ocean-going vessel technology assessment is to provide recommendation on design and implementation of a system that is designed to monitor exhausts from ships while they are in the harbor. This technology will help inform and support CARB planning, regulatory, and monitoring of vessels in the harbor to ensure the goals are met.

<center><h2>Problem Statement</h2></center>
	
In addition to CARB’s efforts to advocate for stricter standards to control local and regional pollutants that impact the health of people living in California port communities, CARB is also focusing on GHG emissions reductions from ocean going vessels. Commercial shipping is the fastest growing sector in terms of GHG emissions. Recognizing the projected adverse effects of global climate change, more aggressive GHG emissions reductions Another effort, the “Green Ship of the Future,” is a collaborative effort seeking to reduce CO2 by 30 percent, sulfur oxides (SOx) by 90 percent, and NOx by 90 percent with the focus on ship design, machinery, propulsion, operation and logistics. Even with scrubbers, catalysts, after treatment methods, or filtration there is no way to verify the exhausts from the ships are in compliant on an ongoing basis. This paper is looking at a solution to give CARB a central location to see information and data they require from the vessel to reach their goals.

<center><h2>Background</h2></center>

Ocean-going vessels (OGV) are large vessels designed for deep-water navigation. Types of OGVs include large cargo vessels such as container vessels, tankers, bulk carriers, and car carriers, as well as passenger cruise vessels. These vessels transport containerized cargo, bulk items such as vehicles, cement, and coke, liquids such as oil and petrochemicals, and passengers. OGVs travel internationally and may be registered by the United States Coast Guard (USCG) as a U.S.-flagged vessel, or under the flag of another country (foreign-flagged vessel). The majority of vessels that visit California ports are foreign-flagged vessels.
OGVs generally have multiple engines and boilers on board. Typically, with the exception of passenger cruise ships; OGVs will have a single large two-stroke main engine used for propulsion, and several smaller four-stroke auxiliary “generator-set” engines. Passenger cruise vessels and some tankers use a different engine configuration referred to as “diesel-electric.” These vessels use large four-stroke diesel generator sets to provide electrical power for both propulsion and ship-board electricity Main engines on OGVs are designed to propel large vessels, thus the engines themselves are much larger than traditional diesel engines. For example, a nine cylinder K98MC-C MAN engine produces about 40 megawatts (MW), enough energy to power 30,000 houses for a year. The 65 feet long by 60 feet high engine is as tall as a five-story building, weighs about 1,500 tons, and costs about $15 million. Main engines are referred to as “Category 3” engines by United States Environmental Protection Agency (U.S. EPA), and have a displacement of greater than 30 liters per cylinder. Auxiliary engines on OGVs generally provide power for uses other than propulsion. They are four-stroke diesel engines that are smaller than the main engines. Most OGVs have more than one auxiliary engine. Auxiliary engines are usually coupled to generators used to produce electrical power. On cargo vessels, most auxiliary engines are used to provide ship-board electricity for lighting, navigation equipment, refrigeration of cargo, and other equipment. Passenger cruise vessels, and some tankers, are unique in that they use auxiliary engines and generator sets to provide electrical power for both propulsion and ship-board electricity. Auxiliary boilers are fuel-fired combustion equipment designed primarily to produce steam for uses other than propulsion, such as heating of residual fuel and liquid cargo, heating of water for crew and passengers, powering steam turbine discharge pumps, freshwater generation, and space heating of cabins. Boilers used to provide propulsion are called steamships and are not included in this assessment because there are very few still in service

<center><h2>Solution</h2></center>

Reader: The unit that will take the serial input and securely send it to the server.<br>
Server: This is the location all the data will be stored.<br>
Web Application: This is where all the Tokens will be managed.<br>

  To avoid having to set up new protocols with each monitoring device manufacturer the Reader will simply connect to the serial output. Many of the available systems have a portal and network capability. If CARB simply built a database with API capabilities each manufacture could design a way of sending the information directly to carb. The reason CARB does not want to go this route is the cost of managing a system that large and complex. This would also require many manufacturers that may not be in the USA to build a separate API communication system for a small number of monitoring systems. Since each monitoring system has their own individual serial output the system would like to connect to that port. The Reader is a piece of hardware designed to take in the serial output from any of the exhaust monitors and securely send it to the server.

Once the vessel is within a geological location the Reader will take the serial output as text and encrypt it using a RSA encryption method. The information will be sent over the network to a server that will stare all the readings from the system. This will not make the information readily available for the public. The server will only collect information. A separate request will need to be made before any information will be made public. This will allow for the vessel owner or agency to communicate before it is made public. Using the portal the vessel owner can generate a Json Web Token. This portal will also act as the UI for the agencies. The system will create a secure way of making data public as long as needed. Once the Ship is done making the exhaust public information the Token will be destroyed and no more information will be able to be collected by the public. The information can still be collected for the vessels records but that information will not be public. If the vessel owner would like to request a dataset based on a timeline a request can be made and Token will be generated for that information.

<h3>Reader Hardware:</h3><br>
Raspberry Pi 4 Model B<br>
	Install Rasbian<br>
	Install Arduino<br>
	Install Teensy 3.6 module for Arduino communication<br>
	Attach a GPS hat<br>
Teensy 3.6<br>
	Install Arduino<br>
Server Setup<br>
Server<br>
Ubuntu Server 18.04.3<br>

<h3>Code Running on the Hardware:</h3><br>
Raspberry Pi<br>
	operating.py<br>
Teensy 3.6<br>
	teensy36.ccp<br>
Server<br>
	server.py<br>
Test Serial output:<br>
raspberry.py<br>
Test Server Communication:<br>
client.py<br>



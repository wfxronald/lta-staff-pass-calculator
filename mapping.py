station_codes = {'Admiralty': 'NS10', 'Aljunied': 'EW9', 'Ang Mo Kio': 'NS16', 'Bakau': 'SE3', 'Bangkit': 'BP9', 'Bartley': 'CC12', 'Bayfront': 'CE1 / DT16', 'Beauty World': 'DT5', 'Bedok': 'EW5', 'Bedok North': 'DT29', 'Bedok Reservoir': 'DT30', 'Bencoolen': 'DT21', 'Bendemeer': 'DT23', 'Bishan': 'NS17 / CC15', 'Boon Keng': 'NE9', 'Boon Lay': 'EW27', 'Botanic Gardens': 'CC19 / DT9', 'Braddell': 'NS18', 'Bras Basah': 'CC2', 'Bright Hill': 'TE7', 'Buangkok': 'NE15', 'Bugis': 'EW12 / DT14', 'Bukit Batok': 'NS2', 'Bukit Gombak': 'NS3', 'Bukit Panjang': 'BP6 / DT1', 'Buona Vista': 'EW21 / CC22', 'Caldecott': 'CC17 / TE9', 'Canberra': 'NS12', 'Cashew': 'DT2', 'Changi Airport': 'CG2', 'Cheng Lim': 'SW1', 'Chinatown': 'NE4 / DT19', 'Chinese Garden': 'EW25', 'Choa Chu Kang': 'NS4 / BP1', 'City Hall': 'NS25 / EW13', 'Clarke Quay': 'NE5', 'Clementi': 'EW23', 'Commonwealth': 'EW20', 'Compassvale': 'SE1', 'Coral Edge': 'PE3', 'Cove': 'PE1', 'Dakota': 'CC8', 'Damai': 'PE7', 'Dhoby Ghaut': 'NS24 / NE6 / CC1', 'Dover': 'EW22', 'Downtown': 'DT17', 'Esplanade': 'CC3', 'Eunos': 'EW7', 'Expo': 'CG1 / DT35', 'Fajar': 'BP10', 'Farmway': 'SW2', 'Farrer Park': 'NE8', 'Farrer Road': 'CC20', 'Fernvale': 'SW5', 'Fort Canning': 'DT20', 'Gardens by the Bay': 'TE22', 'Geylang Bahru': 'DT24', 'Great World': 'TE15', 'Gul Circle': 'EW30', 'HarbourFront': 'NE1 / CC29', 'Havelock': 'TE16', 'Haw Par Villa': 'CC25', 'Hillview': 'DT3', 'Holland Village': 'CC21', 'Hougang': 'NE14', 'Jalan Besar': 'DT22', 'Jelapang': 'BP12', 'Joo Koon': 'EW29', 'Jurong East': 'NS1 / EW24', 'Kadaloor': 'PE5', 'Kaki Bukit': 'DT28', 'Kallang': 'EW10', 'Kangkar': 'SE4', 'Keat Hong': 'BP3', 'Kembangan': 'EW6', 'Kent Ridge': 'CC24', 'Khatib': 'NS14', 'King Albert Park': 'DT6', 'Kovan': 'NE13', 'Kranji': 'NS7', 'Kupang': 'SW3', 'Labrador Park': 'CC27', 'Lakeside': 'EW26', 'Lavender': 'EW11', 'Layar': 'SW6', 'Lentor': 'TE5', 'Little India': 'NE7 / DT12', 'Lorong Chuan': 'CC14', 'MacPherson': 'CC10 / DT26', 'Marina Bay': 'NS27 / TE20 / CE2', 'Marina South Pier': 'NS28', 'Marsiling': 'NS8', 'Marymount': 'CC16', 'Mattar': 'DT25', 'Maxwell': 'TE18', 'Mayflower': 'TE6', 'Meridian': 'PE2', 'Mountbatten': 'CC7', 'Napier': 'TE12', 'Newton': 'NS21 / DT11', 'Nibong': 'PW5', 'Nicoll Highway': 'CC5', 'Novena': 'NS20', 'Oasis': 'PE6', 'one-north': 'CC23', 'Orchard': 'TE14 / NS22', 'Orchard Boulevard': 'TE13', 'Outram Park': 'EW16 / NE3 /TE17', 'Pasir Panjang': 'CC26', 'Pasir Ris': 'EW1', 'Paya Lebar': 'EW8 / CC9', 'Pending': 'BP8', 'Petir': 'BP7', 'Phoenix': 'BP5', 'Pioneer': 'EW28', 'Potong Pasir': 'NE10', 'Promenade': 'CC4 / DT15', 'Punggol': 'NE17 / PTC', 'Punggol Point': 'PW3', 'Queenstown': 'EW19', 'Raffles Place': 'NS26 / EW14', 'Ranggung': 'SE5', 'Redhill': 'EW18', 'Renjong': 'SW8', 'Riviera': 'PE4', 'Rochor': 'DT13', 'Rumbia': 'SE2', 'Sam Kee': 'PW1', 'Samudera': 'PW4', 'Segar': 'BP11', 'Sembawang': 'NS11', 'Sengkang': 'NE16 / STC', 'Senja': 'BP13', 'Serangoon': 'NE12 / CC13', 'Shenton Way': 'TE19', 'Simei': 'EW3', 'Sixth Avenue': 'DT7', 'Somerset': 'NS23', 'Soo Teck': 'PW7', 'South View': 'BP2', 'Springleaf': 'TE4', 'Stadium': 'CC6', 'Stevens': 'DT10 / TE11', 'Sumang': 'PW6', 'Tai Seng': 'CC11', 'Tampines': 'EW2 / DT32', 'Tampines East': 'DT33', 'Tampines West': 'DT31', 'Tan Kah Kee': 'DT8', 'Tanah Merah': 'EW4', 'Tanjong Pagar': 'EW15', 'Teck Whye': 'BP4', 'Telok Ayer': 'DT18', 'Telok Blangah': 'CC28', 'Thanggam': 'SW4', 'Tiong Bahru': 'EW17', 'Toa Payoh': 'NS19', 'Tongkang': 'SW7', 'Tuas Crescent': 'EW31', 'Tuas Link': 'EW33', 'Tuas West Road': 'EW32', 'Ubi': 'DT27', 'Upper Changi': 'DT34', 'Upper Thomson': 'TE8', 'Woodlands North': 'TE1', 'Woodlands': 'NS9 / TE2', 'Woodlands South': 'TE3', 'Woodleigh': 'NE11', 'Yew Tee': 'NS5', 'Yio Chu Kang': 'NS15', 'Yishun': 'NS13'}
irregular_station_names = {
  "Gardens By the Bay": "Gardens by the Bay",
}
irregular_bus_stop_names = {
  # sometimes fuzzywuzzy fails to identify a good option
  "80199 - S'pore Indoor Stadium": "80199 - Stadium Stn",
}
irregular_bus_stop_dir = {
  "410G": "0",
}


def format_station_name(raw_text):
  line_names = ["NSEW", "NEL", "CCL", "DTL", "TEL"]
  final_text = raw_text
  for line in line_names:
    final_text = final_text.replace(line, "")

  final_text = final_text.strip()
  if final_text in irregular_station_names:
    final_text = irregular_station_names[final_text]
  return f"{final_text} ({station_codes[final_text]})"


def format_bus_stop_name(raw_text):
  if raw_text in irregular_bus_stop_names:
    return irregular_bus_stop_names[raw_text]
  return raw_text


def get_bus_direction(trip):
  if trip["BusServiceNo"] in irregular_bus_stop_dir:
    return irregular_bus_stop_dir[trip["BusServiceNo"]]
  # 1-indexed in SimplyGo, 0 indexed in LTA calculator page
  return str(int(trip["BusDirection"][-1]) - 1)

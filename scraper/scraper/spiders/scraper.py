from datetime import datetime
import scrapy
from ..items import ScraperItem

class DataScraper(scrapy.Spider):
    name = "scraper"
    start_urls = ['https://www.amazon.de/dp/1015',
 'https://www.amazon.fr/dp/1015',
 'https://www.amazon.de/dp/000004458X',
 'https://www.amazon.fr/dp/000004458X',
 'https://www.amazon.de/dp/1002198',
 'https://www.amazon.fr/dp/1002198',
 'https://www.amazon.fr/dp/1002791',
 'https://www.amazon.it/dp/1002791',
 'https://www.amazon.de/dp/1002864',
 'https://www.amazon.fr/dp/1002864',
 'https://www.amazon.de/dp/1003704',
 'https://www.amazon.fr/dp/1003704',
 'https://www.amazon.de/dp/1003763',
 'https://www.amazon.fr/dp/1003763',
 'https://www.amazon.fr/dp/1004271',
 'https://www.amazon.it/dp/1004271',
 'https://www.amazon.de/dp/000101742X',
 'https://www.amazon.fr/dp/000101742X',
 'https://www.amazon.de/dp/1017519',
 'https://www.amazon.fr/dp/1017519',
 'https://www.amazon.de/dp/000102163X',
 'https://www.amazon.fr/dp/000102163X',
 'https://www.amazon.fr/dp/1022369',
 'https://www.amazon.it/dp/1022369',
 'https://www.amazon.fr/dp/1022857',
 'https://www.amazon.it/dp/1022857',
 'https://www.amazon.de/dp/1032666',
 'https://www.amazon.fr/dp/1032666',
 'https://www.amazon.de/dp/1034677',
 'https://www.amazon.fr/dp/1034677',
 'https://www.amazon.de/dp/1034936',
 'https://www.amazon.fr/dp/1034936',
 'https://www.amazon.de/dp/1034944',
 'https://www.amazon.fr/dp/1034944',
 'https://www.amazon.de/dp/1035002',
 'https://www.amazon.fr/dp/1035002',
 'https://www.amazon.de/dp/1035029',
 'https://www.amazon.fr/dp/1035029',
 'https://www.amazon.de/dp/1035053',
 'https://www.amazon.es/dp/1035053',
 'https://www.amazon.fr/dp/1035053',
 'https://www.amazon.de/dp/1035339',
 'https://www.amazon.fr/dp/1035339',
 'https://www.amazon.de/dp/1036866',
 'https://www.amazon.es/dp/1036866',
 'https://www.amazon.fr/dp/1036866',
 'https://www.amazon.de/dp/1037137',
 'https://www.amazon.fr/dp/1037137',
 'https://www.amazon.de/dp/1037188',
 'https://www.amazon.fr/dp/1037188',
 'https://www.amazon.de/dp/1037994',
 'https://www.amazon.fr/dp/1037994',
 'https://www.amazon.de/dp/000103863X',
 'https://www.amazon.fr/dp/000103863X',
 'https://www.amazon.de/dp/1039466',
 'https://www.amazon.fr/dp/1039466',
 'https://www.amazon.fr/dp/1040871',
 'https://www.amazon.it/dp/1040871',
 'https://www.amazon.de/dp/1040979',
 'https://www.amazon.fr/dp/1040979',
 'https://www.amazon.de/dp/1040987',
 'https://www.amazon.fr/dp/1040987',
 'https://www.amazon.de/dp/1041002',
 'https://www.amazon.fr/dp/1041002',
 'https://www.amazon.de/dp/1041991',
 'https://www.amazon.fr/dp/1041991',
 'https://www.amazon.de/dp/000104317X',
 'https://www.amazon.fr/dp/000104317X',
 'https://www.amazon.de/dp/1043331',
 'https://www.amazon.fr/dp/1043331',
 'https://www.amazon.de/dp/000104348X',
 'https://www.amazon.fr/dp/000104348X',
 'https://www.amazon.de/dp/1043498',
 'https://www.amazon.fr/dp/1043498',
 'https://www.amazon.de/dp/1043773',
 'https://www.amazon.fr/dp/1043773',
 'https://www.amazon.de/dp/000104396X',
 'https://www.amazon.fr/dp/000104396X',
 'https://www.amazon.de/dp/1048325',
 'https://www.amazon.fr/dp/1048325',
 'https://www.amazon.de/dp/1049119',
 'https://www.amazon.fr/dp/1049119',
 'https://www.amazon.de/dp/1057774',
 'https://www.amazon.fr/dp/1057774',
 'https://www.amazon.de/dp/1057790',
 'https://www.amazon.es/dp/1057790',
 'https://www.amazon.fr/dp/1057790',
 'https://www.amazon.de/dp/1057812',
 'https://www.amazon.es/dp/1057812',
 'https://www.amazon.fr/dp/1057812',
 'https://www.amazon.de/dp/1057987',
 'https://www.amazon.fr/dp/1057987',
 'https://www.amazon.de/dp/1059238',
 'https://www.amazon.fr/dp/1059238',
 'https://www.amazon.de/dp/1060619',
 'https://www.amazon.fr/dp/1060619',
 'https://www.amazon.de/dp/1060694',
 'https://www.amazon.es/dp/1060694',
 'https://www.amazon.fr/dp/1060694',
 'https://www.amazon.de/dp/1061305',
 'https://www.amazon.fr/dp/1061305',
 'https://www.amazon.de/dp/1063685',
 'https://www.amazon.fr/dp/1063685',
 'https://www.amazon.de/dp/1065440',
 'https://www.amazon.fr/dp/1065440',
 'https://www.amazon.de/dp/1065548',
 'https://www.amazon.fr/dp/1065548',
 'https://www.amazon.de/dp/1066544',
 'https://www.amazon.fr/dp/1066544',
 'https://www.amazon.de/dp/1067087',
 'https://www.amazon.fr/dp/1067087',
 'https://www.amazon.de/dp/1067311',
 'https://www.amazon.fr/dp/1067311',
 'https://www.amazon.es/dp/000106875X',
 'https://www.amazon.fr/dp/000106875X',
 'https://www.amazon.it/dp/000106875X',
 'https://www.amazon.de/dp/1069470',
 'https://www.amazon.fr/dp/1069470',
 'https://www.amazon.de/dp/1070991',
 'https://www.amazon.fr/dp/1070991',
 'https://www.amazon.de/dp/000107119X',
 'https://www.amazon.fr/dp/000107119X',
 'https://www.amazon.de/dp/1072064',
 'https://www.amazon.de/dp/1072226',
 'https://www.amazon.fr/dp/1072226',
 'https://www.amazon.de/dp/1072250',
 'https://www.amazon.fr/dp/1072250',
 'https://www.amazon.de/dp/1072498',
 'https://www.amazon.fr/dp/1072498',
 'https://www.amazon.de/dp/1073389',
 'https://www.amazon.fr/dp/1073389',
 'https://www.amazon.de/dp/1073915',
 'https://www.amazon.fr/dp/1073915',
 'https://www.amazon.de/dp/1074504',
 'https://www.amazon.fr/dp/1074504',
 'https://www.amazon.de/dp/1074954',
 'https://www.amazon.fr/dp/1074954',
 'https://www.amazon.de/dp/1075691',
 'https://www.amazon.fr/dp/1075691',
 'https://www.amazon.de/dp/1075969',
 'https://www.amazon.fr/dp/1075969',
 'https://www.amazon.de/dp/1075977',
 'https://www.amazon.fr/dp/1075977',
 'https://www.amazon.de/dp/1077619',
 'https://www.amazon.fr/dp/1077619',
 'https://www.amazon.de/dp/1077732',
 'https://www.amazon.fr/dp/1077732',
 'https://www.amazon.de/dp/1077988',
 'https://www.amazon.fr/dp/1077988',
 'https://www.amazon.de/dp/1078550',
 'https://www.amazon.fr/dp/1078550',
 'https://www.amazon.de/dp/1079131',
 'https://www.amazon.fr/dp/1079131',
 'https://www.amazon.de/dp/1079875',
 'https://www.amazon.fr/dp/1079875',
 'https://www.amazon.de/dp/1080245',
 'https://www.amazon.fr/dp/1080245',
 'https://www.amazon.de/dp/1080350',
 'https://www.amazon.fr/dp/1080350',
 'https://www.amazon.fr/dp/1080601',
 'https://www.amazon.it/dp/1080601',
 'https://www.amazon.de/dp/1080814',
 'https://www.amazon.fr/dp/1080814',
 'https://www.amazon.fr/dp/1081373',
 'https://www.amazon.it/dp/1081373',
 'https://www.amazon.de/dp/000108142X',
 'https://www.amazon.es/dp/000108142X',
 'https://www.amazon.fr/dp/000108142X',
 'https://www.amazon.de/dp/1081470',
 'https://www.amazon.fr/dp/1081470',
 'https://www.amazon.de/dp/000108173X',
 'https://www.amazon.fr/dp/000108173X',
 'https://www.amazon.fr/dp/000108299X',
 'https://www.amazon.it/dp/000108299X',
 'https://www.amazon.de/dp/1083309',
 'https://www.amazon.fr/dp/1083309',
 'https://www.amazon.de/dp/1083414',
 'https://www.amazon.fr/dp/1083414',
 'https://www.amazon.de/dp/1083902',
 'https://www.amazon.fr/dp/1083902',
 'https://www.amazon.de/dp/1084615',
 'https://www.amazon.fr/dp/1084615',
 'https://www.amazon.de/dp/1084704',
 'https://www.amazon.fr/dp/1084704',
 'https://www.amazon.de/dp/1085190',
 'https://www.amazon.fr/dp/1085190',
 'https://www.amazon.fr/dp/1085549',
 'https://www.amazon.it/dp/1085549',
 'https://www.amazon.de/dp/1085727',
 'https://www.amazon.fr/dp/1085727',
 'https://www.amazon.fr/dp/1085840',
 'https://www.amazon.it/dp/1085840',
 'https://www.amazon.fr/dp/1086413',
 'https://www.amazon.it/dp/1086413',
 'https://www.amazon.de/dp/1086553',
 'https://www.amazon.fr/dp/1086553',
 'https://www.amazon.fr/dp/000108657X',
 'https://www.amazon.it/dp/000108657X',
 'https://www.amazon.de/dp/000108660X',
 'https://www.amazon.fr/dp/000108660X',
 'https://www.amazon.de/dp/000108688X',
 'https://www.amazon.fr/dp/000108688X',
 'https://www.amazon.de/dp/1087061',
 'https://www.amazon.fr/dp/1087061',
 'https://www.amazon.de/dp/1087126',
 'https://www.amazon.fr/dp/1087126',
 'https://www.amazon.fr/dp/1087177',
 'https://www.amazon.it/dp/1087177',
 'https://www.amazon.de/dp/1087320',
 'https://www.amazon.fr/dp/1087320',
 'https://www.amazon.de/dp/1087495',
 'https://www.amazon.fr/dp/1087495',
 'https://www.amazon.de/dp/1088114',
 'https://www.amazon.fr/dp/1088114',
 'https://www.amazon.de/dp/1088335',
 'https://www.amazon.fr/dp/1088335',
 'https://www.amazon.fr/dp/1088351',
 'https://www.amazon.it/dp/1088351',
 'https://www.amazon.de/dp/000108898X',
 'https://www.amazon.fr/dp/000108898X',
 'https://www.amazon.fr/dp/1089013',
 'https://www.amazon.it/dp/1089013',
 'https://www.amazon.de/dp/000108917X',
 'https://www.amazon.fr/dp/000108917X',
 'https://www.amazon.de/dp/1089951',
 'https://www.amazon.fr/dp/1089951',
 'https://www.amazon.de/dp/1090224',
 'https://www.amazon.fr/dp/1090224',
 'https://www.amazon.de/dp/1090283',
 'https://www.amazon.fr/dp/1090283',
 'https://www.amazon.de/dp/1090941',
 'https://www.amazon.fr/dp/1090941',
 'https://www.amazon.de/dp/1091182',
 'https://www.amazon.fr/dp/1091182',
 'https://www.amazon.de/dp/1091425',
 'https://www.amazon.fr/dp/1091425',
 'https://www.amazon.de/dp/1091662',
 'https://www.amazon.fr/dp/1091662',
 'https://www.amazon.de/dp/1091832',
 'https://www.amazon.fr/dp/1091832',
 'https://www.amazon.de/dp/1092006',
 'https://www.amazon.fr/dp/1092006',
 'https://www.amazon.de/dp/1092014',
 'https://www.amazon.fr/dp/1092014',
 'https://www.amazon.de/dp/1092049',
 'https://www.amazon.fr/dp/1092049',
 'https://www.amazon.de/dp/000109212X',
 'https://www.amazon.fr/dp/000109212X',
 'https://www.amazon.de/dp/1092138',
 'https://www.amazon.fr/dp/1092138',
 'https://www.amazon.de/dp/1092227',
 'https://www.amazon.fr/dp/1092227',
 'https://www.amazon.de/dp/1092286',
 'https://www.amazon.fr/dp/1092286',
 'https://www.amazon.de/dp/000109257X',
 'https://www.amazon.fr/dp/000109257X',
 'https://www.amazon.de/dp/1093002',
 'https://www.amazon.fr/dp/1093002',
 'https://www.amazon.de/dp/1093134',
 'https://www.amazon.fr/dp/1093134',
 'https://www.amazon.de/dp/1093800',
 'https://www.amazon.fr/dp/1093800',
 'https://www.amazon.de/dp/000109453X',
 'https://www.amazon.fr/dp/000109453X',
 'https://www.amazon.de/dp/1094556',
 'https://www.amazon.fr/dp/1094556',
 'https://www.amazon.de/dp/1094580',
 'https://www.amazon.fr/dp/1094580',
 'https://www.amazon.de/dp/1095072',
 'https://www.amazon.fr/dp/1095072',
 'https://www.amazon.de/dp/1095293',
 'https://www.amazon.fr/dp/1095293',
 'https://www.amazon.de/dp/1095579',
 'https://www.amazon.fr/dp/1095579',
 'https://www.amazon.de/dp/1095951',
 'https://www.amazon.fr/dp/1095951',
 'https://www.amazon.fr/dp/1096168',
 'https://www.amazon.it/dp/1096168',
 'https://www.amazon.de/dp/1096303',
 'https://www.amazon.fr/dp/1096303',
 'https://www.amazon.de/dp/1096478',
 'https://www.amazon.fr/dp/1096478',
 'https://www.amazon.de/dp/1097784',
 'https://www.amazon.fr/dp/1097784',
 'https://www.amazon.de/dp/000109825X',
 'https://www.amazon.fr/dp/000109825X',
 'https://www.amazon.de/dp/1098284',
 'https://www.amazon.fr/dp/1098284',
 'https://www.amazon.de/dp/1098691',
 'https://www.amazon.fr/dp/1098691',
 'https://www.amazon.fr/dp/1099183',
 'https://www.amazon.it/dp/1099183',
 'https://www.amazon.de/dp/1099515',
 'https://www.amazon.fr/dp/1099515',
 'https://www.amazon.fr/dp/1100505',
 'https://www.amazon.it/dp/1100505',
 'https://www.amazon.de/dp/1100726',
 'https://www.amazon.fr/dp/1100726',
 'https://www.amazon.de/dp/1100742',
 'https://www.amazon.fr/dp/1100742',
 'https://www.amazon.de/dp/1100777',
 'https://www.amazon.fr/dp/1100777',
 'https://www.amazon.de/dp/1102249',
 'https://www.amazon.fr/dp/1102249',
 'https://www.amazon.de/dp/1103148',
 'https://www.amazon.fr/dp/1103148',
 'https://www.amazon.de/dp/1103369',
 'https://www.amazon.fr/dp/1103369',
 'https://www.amazon.de/dp/1106538',
 'https://www.amazon.fr/dp/1106538',
 'https://www.amazon.de/dp/1106597',
 'https://www.amazon.fr/dp/1106597',
 'https://www.amazon.de/dp/1106740',
 'https://www.amazon.fr/dp/1106740',
 'https://www.amazon.de/dp/1106775',
 'https://www.amazon.fr/dp/1106775',
 'https://www.amazon.de/dp/1106929',
 'https://www.amazon.fr/dp/1106929',
 'https://www.amazon.de/dp/1106996',
 'https://www.amazon.fr/dp/1106996',
 'https://www.amazon.de/dp/1107046',
 'https://www.amazon.fr/dp/1107046',
 'https://www.amazon.de/dp/1107178',
 'https://www.amazon.fr/dp/1107178',
 'https://www.amazon.de/dp/1107267',
 'https://www.amazon.fr/dp/1107267',
 'https://www.amazon.de/dp/000110733X',
 'https://www.amazon.fr/dp/000110733X',
 'https://www.amazon.de/dp/1109596',
 'https://www.amazon.fr/dp/1109596',
 'https://www.amazon.de/dp/1109634',
 'https://www.amazon.fr/dp/1109634',
 'https://www.amazon.de/dp/1109693',
 'https://www.amazon.fr/dp/1109693',
 'https://www.amazon.de/dp/1109723',
 'https://www.amazon.es/dp/1109723',
 'https://www.amazon.fr/dp/1109723',
 'https://www.amazon.fr/dp/1112031',
 'https://www.amazon.it/dp/1112031',
 'https://www.amazon.de/dp/000111252X',
 'https://www.amazon.fr/dp/000111252X',
 'https://www.amazon.de/dp/1113623',
 'https://www.amazon.fr/dp/1113623',
 'https://www.amazon.de/dp/1113844',
 'https://www.amazon.fr/dp/1113844',
 'https://www.amazon.de/dp/1115626',
 'https://www.amazon.fr/dp/1115626',
 'https://www.amazon.de/dp/1115707',
 'https://www.amazon.fr/dp/1115707',
 'https://www.amazon.de/dp/1117823',
 'https://www.amazon.fr/dp/1117823',
 'https://www.amazon.de/dp/1120409',
 'https://www.amazon.fr/dp/1120409',
 'https://www.amazon.de/dp/1120972',
 'https://www.amazon.fr/dp/1120972',
 'https://www.amazon.de/dp/1121790',
 'https://www.amazon.fr/dp/1121790',
 'https://www.amazon.de/dp/1123335',
 'https://www.amazon.fr/dp/1123335',
 'https://www.amazon.de/dp/1123734',
 'https://www.amazon.fr/dp/1123734',
 'https://www.amazon.de/dp/1126334',
 'https://www.amazon.fr/dp/1126334',
 'https://www.amazon.de/dp/1126350',
 'https://www.amazon.fr/dp/1126350',
 'https://www.amazon.de/dp/1128876',
 'https://www.amazon.fr/dp/1128876',
 'https://www.amazon.de/dp/1130072',
 'https://www.amazon.fr/dp/1130072',
 'https://www.amazon.de/dp/1130951',
 'https://www.amazon.fr/dp/1130951',
 'https://www.amazon.de/dp/1131273',
 'https://www.amazon.fr/dp/1131273',
 'https://www.amazon.de/dp/1131427',
 'https://www.amazon.fr/dp/1131427',
 'https://www.amazon.de/dp/1132814',
 'https://www.amazon.fr/dp/1132814',
 'https://www.amazon.de/dp/1133705',
 'https://www.amazon.fr/dp/1133705',
 'https://www.amazon.de/dp/1137727',
 'https://www.amazon.fr/dp/1137727',
 'https://www.amazon.de/dp/1137999',
 'https://www.amazon.fr/dp/1137999',
 'https://www.amazon.de/dp/1138235',
 'https://www.amazon.fr/dp/1138235',
 'https://www.amazon.de/dp/1139371',
 'https://www.amazon.fr/dp/1139371',
 'https://www.amazon.de/dp/1139398',
 'https://www.amazon.fr/dp/1139398',
 'https://www.amazon.fr/dp/1140795',
 'https://www.amazon.it/dp/1140795',
 'https://www.amazon.de/dp/1141341',
 'https://www.amazon.es/dp/1141341',
 'https://www.amazon.fr/dp/1141341',
 'https://www.amazon.de/dp/1144553',
 'https://www.amazon.fr/dp/1144553',
 'https://www.amazon.de/dp/1144634',
 'https://www.amazon.fr/dp/1144634',
 'https://www.amazon.de/dp/1144685',
 'https://www.amazon.fr/dp/1144685',
 'https://www.amazon.de/dp/1145452',
 'https://www.amazon.fr/dp/1145452',
 'https://www.amazon.de/dp/1147102',
 'https://www.amazon.fr/dp/1147102',
 'https://www.amazon.de/dp/1148516',
 'https://www.amazon.fr/dp/1148516',
 'https://www.amazon.de/dp/1149458',
 'https://www.amazon.fr/dp/1149458',
 'https://www.amazon.de/dp/1150251',
 'https://www.amazon.fr/dp/1150251',
 'https://www.amazon.de/dp/1150456',
 'https://www.amazon.fr/dp/1150456',
 'https://www.amazon.fr/dp/1151827',
 'https://www.amazon.it/dp/1151827',
 'https://www.amazon.de/dp/1152661',
 'https://www.amazon.fr/dp/1152661',
 'https://www.amazon.de/dp/1153226',
 'https://www.amazon.fr/dp/1153226',
 'https://www.amazon.de/dp/1153234',
 'https://www.amazon.fr/dp/1153234',
 'https://www.amazon.de/dp/1154036',
 'https://www.amazon.fr/dp/1154036',
 'https://www.amazon.de/dp/000115687X',
 'https://www.amazon.fr/dp/000115687X',
 'https://www.amazon.de/dp/1157078',
 'https://www.amazon.fr/dp/1157078',
 'https://www.amazon.fr/dp/1157981',
 'https://www.amazon.it/dp/1157981',
 'https://www.amazon.de/dp/1168061',
 'https://www.amazon.fr/dp/1168061',
 'https://www.amazon.de/dp/1168266',
 'https://www.amazon.fr/dp/1168266',
 'https://www.amazon.de/dp/1170481',
 'https://www.amazon.fr/dp/1170481',
 'https://www.amazon.de/dp/1171135',
 'https://www.amazon.fr/dp/1171135',
 'https://www.amazon.de/dp/1171550',
 'https://www.amazon.fr/dp/1171550',
 'https://www.amazon.de/dp/1172093',
 'https://www.amazon.fr/dp/1172093',
 'https://www.amazon.de/dp/1172484',
 'https://www.amazon.fr/dp/1172484',
 'https://www.amazon.de/dp/1177737',
 'https://www.amazon.fr/dp/1177737',
 'https://www.amazon.de/dp/1178490',
 'https://www.amazon.fr/dp/1178490',
 'https://www.amazon.de/dp/1189662',
 'https://www.amazon.fr/dp/1189662',
 'https://www.amazon.de/dp/1190903',
 'https://www.amazon.fr/dp/1190903',
 'https://www.amazon.de/dp/1193287',
 'https://www.amazon.fr/dp/1193287',
 'https://www.amazon.de/dp/1195883',
 'https://www.amazon.fr/dp/1195883',
 'https://www.amazon.de/dp/1199013',
 'https://www.amazon.fr/dp/1199013',
 'https://www.amazon.de/dp/1200534',
 'https://www.amazon.fr/dp/1200534',
 'https://www.amazon.de/dp/1201344',
 'https://www.amazon.fr/dp/1201344',
 'https://www.amazon.de/dp/1202405',
 'https://www.amazon.fr/dp/1202405',
 'https://www.amazon.de/dp/1203231',
 'https://www.amazon.fr/dp/1203231',
 'https://www.amazon.de/dp/2000970',
 'https://www.amazon.fr/dp/2000970',
 'https://www.amazon.de/dp/4130251',
 'https://www.amazon.fr/dp/4130251',
 'https://www.amazon.de/dp/4132505',
 'https://www.amazon.fr/dp/4132505',
 'https://www.amazon.de/dp/4160177',
 'https://www.amazon.fr/dp/4160177',
 'https://www.amazon.de/dp/4160266',
 'https://www.amazon.fr/dp/4160266',
 'https://www.amazon.de/dp/4160398',
 'https://www.amazon.fr/dp/4160398',
 'https://www.amazon.de/dp/4160401',
 'https://www.amazon.fr/dp/4160401',
 'https://www.amazon.de/dp/000416041X',
 'https://www.amazon.fr/dp/000416041X',
 'https://www.amazon.de/dp/4160592',
 'https://www.amazon.fr/dp/4160592',
 'https://www.amazon.de/dp/4160665',
 'https://www.amazon.fr/dp/4160665',
 'https://www.amazon.de/dp/4160673',
 'https://www.amazon.fr/dp/4160673',
 'https://www.amazon.de/dp/4160800',
 'https://www.amazon.fr/dp/4160800',
 'https://www.amazon.de/dp/4160886',
 'https://www.amazon.fr/dp/4160886',
 'https://www.amazon.de/dp/4161041',
 'https://www.amazon.fr/dp/4161041',
 'https://www.amazon.de/dp/000416105X',
 'https://www.amazon.fr/dp/000416105X',
 'https://www.amazon.de/dp/4161114',
 'https://www.amazon.fr/dp/4161114',
 'https://www.amazon.de/dp/4161130',
 'https://www.amazon.fr/dp/4161130',
 'https://www.amazon.de/dp/4161149',
 'https://www.amazon.fr/dp/4161149',
 'https://www.amazon.de/dp/4161262',
 'https://www.amazon.fr/dp/4161262',
 'https://www.amazon.de/dp/4161475',
 'https://www.amazon.fr/dp/4161475',
 'https://www.amazon.de/dp/4161858',
 'https://www.amazon.fr/dp/4161858',
 'https://www.amazon.de/dp/4161939',
 'https://www.amazon.fr/dp/4161939',
 'https://www.amazon.de/dp/4161955',
 'https://www.amazon.fr/dp/4161955',
 'https://www.amazon.fr/dp/000416198X',
 'https://www.amazon.it/dp/000416198X',
 'https://www.amazon.de/dp/4162064',
 'https://www.amazon.fr/dp/4162064',
 'https://www.amazon.de/dp/4162072',
 'https://www.amazon.fr/dp/4162072',
 'https://www.amazon.de/dp/4162188',
 'https://www.amazon.fr/dp/4162188',
 'https://www.amazon.de/dp/4162358',
 'https://www.amazon.fr/dp/4162358',
 'https://www.amazon.de/dp/4162552',
 'https://www.amazon.fr/dp/4162552',
 'https://www.amazon.de/dp/4162811',
 'https://www.amazon.fr/dp/4162811',
 'https://www.amazon.de/dp/4162838',
 'https://www.amazon.fr/dp/4162838',
 'https://www.amazon.de/dp/4162854',
 'https://www.amazon.fr/dp/4162854',
 'https://www.amazon.de/dp/4163230',
 'https://www.amazon.fr/dp/4163230',
 'https://www.amazon.de/dp/4163524',
 'https://www.amazon.fr/dp/4163524',
 'https://www.amazon.de/dp/4163583',
 'https://www.amazon.fr/dp/4163583',
 'https://www.amazon.it/dp/4163583',
 'https://www.amazon.de/dp/4163621',
 'https://www.amazon.fr/dp/4163621',
 'https://www.amazon.de/dp/4163737',
 'https://www.amazon.fr/dp/4163737',
 'https://www.amazon.de/dp/4163788',
 'https://www.amazon.fr/dp/4163788',
 'https://www.amazon.fr/dp/4163923',
 'https://www.amazon.it/dp/4163923',
 'https://www.amazon.de/dp/4164016',
 'https://www.amazon.fr/dp/4164016',
 'https://www.amazon.de/dp/000416413X',
 'https://www.amazon.fr/dp/000416413X',
 'https://www.amazon.de/dp/000416444X',
 'https://www.amazon.fr/dp/000416444X',
 'https://www.amazon.de/dp/4164474',
 'https://www.amazon.fr/dp/4164474',
 'https://www.amazon.de/dp/4164482',
 'https://www.amazon.fr/dp/4164482',
 'https://www.amazon.de/dp/4164598',
 'https://www.amazon.fr/dp/4164598',
 'https://www.amazon.de/dp/4164830',
 'https://www.amazon.fr/dp/4164830',
 'https://www.amazon.de/dp/4164938',
 'https://www.amazon.fr/dp/4164938',
 'https://www.amazon.de/dp/000416508X',
 'https://www.amazon.fr/dp/000416508X',
 'https://www.amazon.de/dp/000416511X',
 'https://www.amazon.fr/dp/000416511X',
 'https://www.amazon.de/dp/4165829',
 'https://www.amazon.fr/dp/4165829',
 'https://www.amazon.de/dp/4165845',
 'https://www.amazon.fr/dp/4165845',
 'https://www.amazon.de/dp/4166345',
 'https://www.amazon.fr/dp/4166345',
 'https://www.amazon.fr/dp/4166523',
 'https://www.amazon.it/dp/4166523',
 'https://www.amazon.de/dp/4167082',
 'https://www.amazon.fr/dp/4167082',
 'https://www.amazon.de/dp/4167384',
 'https://www.amazon.fr/dp/4167384',
 'https://www.amazon.de/dp/4167465',
 'https://www.amazon.fr/dp/4167465',
 'https://www.amazon.de/dp/4167848',
 'https://www.amazon.fr/dp/4167848',
 'https://www.amazon.fr/dp/000416816X',
 'https://www.amazon.it/dp/000416816X',
 'https://www.amazon.de/dp/4168240',
 'https://www.amazon.fr/dp/4168240',
 'https://www.amazon.de/dp/4168275',
 'https://www.amazon.fr/dp/4168275',
 'https://www.amazon.de/dp/4168615',
 'https://www.amazon.fr/dp/4168615',
 'https://www.amazon.de/dp/4168631',
 'https://www.amazon.fr/dp/4168631',
 'https://www.amazon.de/dp/4169115',
 'https://www.amazon.fr/dp/4169115',
 'https://www.amazon.de/dp/4169573',
 'https://www.amazon.fr/dp/4169573',
 'https://www.amazon.fr/dp/4169646',
 'https://www.amazon.it/dp/4169646',
 'https://www.amazon.de/dp/4169662',
 'https://www.amazon.fr/dp/4169662',
 'https://www.amazon.fr/dp/4169751',
 'https://www.amazon.it/dp/4169751',
 'https://www.amazon.de/dp/000416976X',
 'https://www.amazon.fr/dp/000416976X',
 'https://www.amazon.de/dp/4169786',
 'https://www.amazon.fr/dp/4169786',
 'https://www.amazon.fr/dp/4169859',
 'https://www.amazon.it/dp/4169859',
 'https://www.amazon.de/dp/4170342',
 'https://www.amazon.fr/dp/4170342',
 'https://www.amazon.de/dp/4171055',
 'https://www.amazon.fr/dp/4171055',
 'https://www.amazon.de/dp/4171128',
 'https://www.amazon.fr/dp/4171128',
 'https://www.amazon.de/dp/4171187',
 'https://www.amazon.fr/dp/4171187',
 'https://www.amazon.de/dp/4171195',
 'https://www.amazon.fr/dp/4171195',
 'https://www.amazon.de/dp/4171330',
 'https://www.amazon.fr/dp/4171330',
 'https://www.amazon.de/dp/000417156X',
 'https://www.amazon.fr/dp/000417156X',
 'https://www.amazon.de/dp/4171578',
 'https://www.amazon.fr/dp/4171578',
 'https://www.amazon.de/dp/4171608',
 'https://www.amazon.fr/dp/4171608',
 'https://www.amazon.de/dp/4171675',
 'https://www.amazon.fr/dp/4171675',
 'https://www.amazon.de/dp/4171683',
 'https://www.amazon.fr/dp/4171683',
 'https://www.amazon.de/dp/4171691',
 'https://www.amazon.fr/dp/4171691',
 'https://www.amazon.de/dp/4171713',
 'https://www.amazon.fr/dp/4171713',
 'https://www.amazon.de/dp/000417173X',
 'https://www.amazon.fr/dp/000417173X',
 'https://www.amazon.de/dp/4171780',
 'https://www.amazon.fr/dp/4171780',
 'https://www.amazon.de/dp/4171802',
 'https://www.amazon.fr/dp/4171802',
 'https://www.amazon.de/dp/4171853',
 'https://www.amazon.fr/dp/4171853',
 'https://www.amazon.de/dp/4171985',
 'https://www.amazon.fr/dp/4171985',
 'https://www.amazon.de/dp/4172019',
 'https://www.amazon.fr/dp/4172019',
 'https://www.amazon.de/dp/4172043',
 'https://www.amazon.fr/dp/4172043',
 'https://www.amazon.de/dp/000417206X',
 'https://www.amazon.fr/dp/000417206X',
 'https://www.amazon.de/dp/4172078',
 'https://www.amazon.fr/dp/4172078',
 'https://www.amazon.de/dp/4172175',
 'https://www.amazon.fr/dp/4172175',
 'https://www.amazon.de/dp/4172191',
 'https://www.amazon.fr/dp/4172191',
 'https://www.amazon.de/dp/4172256',
 'https://www.amazon.fr/dp/4172256',
 'https://www.amazon.de/dp/4172264',
 'https://www.amazon.fr/dp/4172264',
 'https://www.amazon.de/dp/4172302',
 'https://www.amazon.fr/dp/4172302',
 'https://www.amazon.de/dp/4172353',
 'https://www.amazon.fr/dp/4172353',
 'https://www.amazon.de/dp/000417237X',
 'https://www.amazon.fr/dp/000417237X',
 'https://www.amazon.de/dp/4172396',
 'https://www.amazon.fr/dp/4172396',
 'https://www.amazon.de/dp/000417240X',
 'https://www.amazon.fr/dp/000417240X',
 'https://www.amazon.de/dp/4172426',
 'https://www.amazon.fr/dp/4172426',
 'https://www.amazon.de/dp/4172442',
 'https://www.amazon.fr/dp/4172442',
 'https://www.amazon.de/dp/4172469',
 'https://www.amazon.fr/dp/4172469',
 'https://www.amazon.de/dp/4172507',
 'https://www.amazon.fr/dp/4172507',
 'https://www.amazon.de/dp/4172515',
 'https://www.amazon.fr/dp/4172515',
 'https://www.amazon.de/dp/4172558',
 'https://www.amazon.fr/dp/4172558',
 'https://www.amazon.de/dp/4172566',
 'https://www.amazon.fr/dp/4172566',
 'https://www.amazon.de/dp/4172612',
 'https://www.amazon.fr/dp/4172612',
 'https://www.amazon.de/dp/4172620',
 'https://www.amazon.fr/dp/4172620',
 'https://www.amazon.de/dp/4172655',
 'https://www.amazon.fr/dp/4172655',
 'https://www.amazon.de/dp/4172671',
 'https://www.amazon.fr/dp/4172671',
 'https://www.amazon.de/dp/000417268X',
 'https://www.amazon.fr/dp/000417268X',
 'https://www.amazon.de/dp/4172698',
 'https://www.amazon.fr/dp/4172698',
 'https://www.amazon.de/dp/4172701',
 'https://www.amazon.fr/dp/4172701',
 'https://www.amazon.de/dp/000417271X',
 'https://www.amazon.fr/dp/000417271X',
 'https://www.amazon.de/dp/4172736',
 'https://www.amazon.fr/dp/4172736',
 'https://www.amazon.de/dp/4172744',
 'https://www.amazon.fr/dp/4172744',
 'https://www.amazon.de/dp/4172833',
 'https://www.amazon.fr/dp/4172833',
 'https://www.amazon.de/dp/4172841',
 'https://www.amazon.fr/dp/4172841',
 'https://www.amazon.de/dp/4172884',
 'https://www.amazon.fr/dp/4172884',
 'https://www.amazon.de/dp/4172906',
 'https://www.amazon.fr/dp/4172906',
 'https://www.amazon.de/dp/4172922',
 'https://www.amazon.fr/dp/4172922',
 'https://www.amazon.de/dp/4172930',
 'https://www.amazon.fr/dp/4172930',
 'https://www.amazon.de/dp/4172957',
 'https://www.amazon.fr/dp/4172957',
 'https://www.amazon.de/dp/4172973',
 'https://www.amazon.fr/dp/4172973',
 'https://www.amazon.de/dp/4173082',
 'https://www.amazon.fr/dp/4173082',
 'https://www.amazon.de/dp/4173090',
 'https://www.amazon.fr/dp/4173090',
 'https://www.amazon.de/dp/4173120',
 'https://www.amazon.fr/dp/4173120',
 'https://www.amazon.de/dp/4173163',
 'https://www.amazon.fr/dp/4173163',
 'https://www.amazon.de/dp/000417318X',
 'https://www.amazon.fr/dp/000417318X',
 'https://www.amazon.de/dp/4173198',
 'https://www.amazon.fr/dp/4173198',
 'https://www.amazon.de/dp/4173201',
 'https://www.amazon.fr/dp/4173201',
 'https://www.amazon.de/dp/4173228',
 'https://www.amazon.fr/dp/4173228',
 'https://www.amazon.de/dp/4173252',
 'https://www.amazon.fr/dp/4173252',
 'https://www.amazon.de/dp/4173295',
 'https://www.amazon.fr/dp/4173295',
 'https://www.amazon.de/dp/4173309',
 'https://www.amazon.fr/dp/4173309',
 'https://www.amazon.de/dp/4173325',
 'https://www.amazon.fr/dp/4173325',
 'https://www.amazon.de/dp/4173333',
 'https://www.amazon.fr/dp/4173333',
 'https://www.amazon.de/dp/000417335X',
 'https://www.amazon.fr/dp/000417335X',
 'https://www.amazon.de/dp/4173376',
 'https://www.amazon.fr/dp/4173376',
 'https://www.amazon.de/dp/4173384',
 'https://www.amazon.fr/dp/4173384',
 'https://www.amazon.de/dp/4173406',
 'https://www.amazon.fr/dp/4173406',
 'https://www.amazon.de/dp/4173430',
 'https://www.amazon.fr/dp/4173430',
 'https://www.amazon.de/dp/4173473',
 'https://www.amazon.fr/dp/4173473',
 'https://www.amazon.de/dp/4173538',
 'https://www.amazon.fr/dp/4173538',
 'https://www.amazon.de/dp/4173589',
 'https://www.amazon.fr/dp/4173589',
 'https://www.amazon.de/dp/4173643',
 'https://www.amazon.fr/dp/4173643',
 'https://www.amazon.de/dp/4173899',
 'https://www.amazon.fr/dp/4173899',
 'https://www.amazon.de/dp/4174194',
 'https://www.amazon.fr/dp/4174194',
 'https://www.amazon.de/dp/4174348',
 'https://www.amazon.fr/dp/4174348',
 'https://www.amazon.de/dp/4174380',
 'https://www.amazon.fr/dp/4174380',
 'https://www.amazon.it/dp/4174380',
 'https://www.amazon.fr/dp/4174399',
 'https://www.amazon.it/dp/4174399',
 'https://www.amazon.de/dp/4174453',
 'https://www.amazon.fr/dp/4174453',
 'https://www.amazon.fr/dp/4174496',
 'https://www.amazon.it/dp/4174496',
 'https://www.amazon.de/dp/4174518',
 'https://www.amazon.fr/dp/4174518',
 'https://www.amazon.de/dp/4174542',
 'https://www.amazon.fr/dp/4174542',
 'https://www.amazon.de/dp/4174933',
 'https://www.amazon.fr/dp/4174933',
 'https://www.amazon.de/dp/4175360',
 'https://www.amazon.fr/dp/4175360',
 'https://www.amazon.de/dp/4175387',
 'https://www.amazon.fr/dp/4175387',
 'https://www.amazon.de/dp/4175522',
 'https://www.amazon.fr/dp/4175522',
 'https://www.amazon.de/dp/4175778',
 'https://www.amazon.fr/dp/4175778',
 'https://www.amazon.de/dp/4175794',
 'https://www.amazon.fr/dp/4175794',
 'https://www.amazon.de/dp/4175816',
 'https://www.amazon.fr/dp/4175816',
 'https://www.amazon.de/dp/4175972',
 'https://www.amazon.fr/dp/4175972',
 'https://www.amazon.de/dp/4176170',
 'https://www.amazon.fr/dp/4176170',
 'https://www.amazon.de/dp/4176324',
 'https://www.amazon.fr/dp/4176324',
 'https://www.amazon.fr/dp/4176367',
 'https://www.amazon.it/dp/4176367',
 'https://www.amazon.fr/dp/4176421',
 'https://www.amazon.it/dp/4176421',
 'https://www.amazon.de/dp/4176448',
 'https://www.amazon.fr/dp/4176448',
 'https://www.amazon.de/dp/4176731',
 'https://www.amazon.fr/dp/4176731',
 'https://www.amazon.de/dp/4176839',
 'https://www.amazon.fr/dp/4176839',
 'https://www.amazon.de/dp/4176847',
 'https://www.amazon.fr/dp/4176847',
 'https://www.amazon.de/dp/4176960',
 'https://www.amazon.fr/dp/4176960',
 'https://www.amazon.de/dp/4176995',
 'https://www.amazon.fr/dp/4176995',
 'https://www.amazon.de/dp/4177118',
 'https://www.amazon.fr/dp/4177118',
 'https://www.amazon.de/dp/4177134',
 'https://www.amazon.fr/dp/4177134',
 'https://www.amazon.de/dp/4177347',
 'https://www.amazon.fr/dp/4177347',
 'https://www.amazon.fr/dp/4177371',
 'https://www.amazon.it/dp/4177371',
 'https://www.amazon.fr/dp/4177649',
 'https://www.amazon.it/dp/4177649',
 'https://www.amazon.de/dp/4177940',
 'https://www.amazon.fr/dp/4177940',
 'https://www.amazon.de/dp/4177967',
 'https://www.amazon.fr/dp/4177967',
 'https://www.amazon.de/dp/4177975',
 'https://www.amazon.fr/dp/4177975',
 'https://www.amazon.de/dp/4178033',
 'https://www.amazon.fr/dp/4178033',
 'https://www.amazon.de/dp/000417805X',
 'https://www.amazon.fr/dp/000417805X',
 'https://www.amazon.de/dp/4178084',
 'https://www.amazon.fr/dp/4178084',
 'https://www.amazon.de/dp/4178459',
 'https://www.amazon.fr/dp/4178459',
 'https://www.amazon.de/dp/4178491',
 'https://www.amazon.fr/dp/4178491',
 'https://www.amazon.de/dp/4178564',
 'https://www.amazon.fr/dp/4178564',
 'https://www.amazon.de/dp/4178645',
 'https://www.amazon.fr/dp/4178645',
 'https://www.amazon.de/dp/000417870X',
 'https://www.amazon.fr/dp/000417870X',
 'https://www.amazon.de/dp/4178750',
 'https://www.amazon.fr/dp/4178750',
 'https://www.amazon.de/dp/4179943',
 'https://www.amazon.fr/dp/4179943',
 'https://www.amazon.fr/dp/4180542',
 'https://www.amazon.it/dp/4180542',
 'https://www.amazon.de/dp/4182154',
 'https://www.amazon.de/dp/4182170',
 'https://www.amazon.fr/dp/4182170',
 'https://www.amazon.de/dp/4182197',
 'https://www.amazon.fr/dp/4182197',
 'https://www.amazon.de/dp/4182510',
 'https://www.amazon.fr/dp/4182510',
 'https://www.amazon.de/dp/4182634',
 'https://www.amazon.fr/dp/4182634',
 'https://www.amazon.de/dp/4183614',
 'https://www.amazon.fr/dp/4183614',
 'https://www.amazon.de/dp/4184289',
 'https://www.amazon.fr/dp/4184289',
 'https://www.amazon.de/dp/4184866',
 'https://www.amazon.fr/dp/4184866',
 'https://www.amazon.de/dp/4200101',
 'https://www.amazon.fr/dp/4200101',
 'https://www.amazon.de/dp/4200128',
 'https://www.amazon.fr/dp/4200128',
 'https://www.amazon.de/dp/4200624',
 'https://www.amazon.fr/dp/4200624',
 'https://www.amazon.it/dp/4200624',
 'https://www.amazon.de/dp/4200675',
 'https://www.amazon.fr/dp/4200675',
 'https://www.amazon.de/dp/4200756',
 'https://www.amazon.fr/dp/4200756',
 'https://www.amazon.de/dp/4200764',
 'https://www.amazon.fr/dp/4200764',
 'https://www.amazon.de/dp/4201183',
 'https://www.amazon.fr/dp/4201183',
 'https://www.amazon.fr/dp/4201604',
 'https://www.amazon.it/dp/4201604',
 'https://www.amazon.de/dp/4201612',
 'https://www.amazon.fr/dp/4201612',
 'https://www.amazon.de/dp/4202406',
 'https://www.amazon.fr/dp/4202406',
 'https://www.amazon.de/dp/4206827',
 'https://www.amazon.fr/dp/4206827',
 'https://www.amazon.de/dp/4207181',
 'https://www.amazon.fr/dp/4207181',
 'https://www.amazon.de/dp/000420736X',
 'https://www.amazon.fr/dp/000420736X',
 'https://www.amazon.de/dp/4208625',
 'https://www.amazon.fr/dp/4208625',
 'https://www.amazon.de/dp/4209508',
 'https://www.amazon.fr/dp/4209508',
 'https://www.amazon.de/dp/4209656',
 'https://www.amazon.fr/dp/4209656',
 'https://www.amazon.de/dp/4210778',
 'https://www.amazon.fr/dp/4210778',
 'https://www.amazon.de/dp/4211170',
 'https://www.amazon.fr/dp/4211170',
 'https://www.amazon.de/dp/4211308',
 'https://www.amazon.fr/dp/4211308',
 'https://www.amazon.de/dp/4211421',
 'https://www.amazon.fr/dp/4211421',
 'https://www.amazon.de/dp/000421143X',
 'https://www.amazon.fr/dp/000421143X',
 'https://www.amazon.de/dp/4211472',
 'https://www.amazon.fr/dp/4211472',
 'https://www.amazon.de/dp/4211596',
 'https://www.amazon.fr/dp/4211596',
 'https://www.amazon.de/dp/4211618',
 'https://www.amazon.fr/dp/4211618',
 'https://www.amazon.de/dp/4211634',
 'https://www.amazon.fr/dp/4211634',
 'https://www.amazon.de/dp/4211650',
 'https://www.amazon.fr/dp/4211650',
 'https://www.amazon.de/dp/4211669',
 'https://www.amazon.fr/dp/4211669',
 'https://www.amazon.de/dp/4211715',
 'https://www.amazon.fr/dp/4211715',
 'https://www.amazon.de/dp/4211723',
 'https://www.amazon.fr/dp/4211723',
 'https://www.amazon.de/dp/4211782',
 'https://www.amazon.fr/dp/4211782',
 'https://www.amazon.de/dp/4211812',
 'https://www.amazon.fr/dp/4211812',
 'https://www.amazon.de/dp/4211855',
 'https://www.amazon.fr/dp/4211855',
 'https://www.amazon.de/dp/4211863',
 'https://www.amazon.fr/dp/4211863',
 'https://www.amazon.de/dp/4212029',
 'https://www.amazon.fr/dp/4212029',
 'https://www.amazon.de/dp/4480007',
 'https://www.amazon.fr/dp/4480007',
 'https://www.amazon.de/dp/4480422',
 'https://www.amazon.fr/dp/4480422',
 'https://www.amazon.fr/dp/4480570',
 'https://www.amazon.it/dp/4480570',
 'https://www.amazon.de/dp/4481127',
 'https://www.amazon.fr/dp/4481127',
 'https://www.amazon.de/dp/4481429',
 'https://www.amazon.fr/dp/4481429',
 'https://www.amazon.de/dp/4482093',
 'https://www.amazon.fr/dp/4482093',
 'https://www.amazon.fr/dp/4482174',
 'https://www.amazon.it/dp/4482174',
 'https://www.amazon.fr/dp/4482190',
 'https://www.amazon.it/dp/4482190',
 'https://www.amazon.fr/dp/4482204',
 'https://www.amazon.it/dp/4482204',
 'https://www.amazon.de/dp/4484029',
 'https://www.amazon.fr/dp/4484029',
 'https://www.amazon.de/dp/4484320',
 'https://www.amazon.fr/dp/4484320',
 'https://www.amazon.de/dp/4484339',
 'https://www.amazon.fr/dp/4484339',
 'https://www.amazon.de/dp/4484347',
 'https://www.amazon.fr/dp/4484347',
 'https://www.amazon.fr/dp/4484355',
 'https://www.amazon.it/dp/4484355',
 'https://www.amazon.de/dp/4484428',
 'https://www.amazon.fr/dp/4484428',
 'https://www.amazon.de/dp/4484436',
 'https://www.amazon.fr/dp/4484436',
 'https://www.amazon.fr/dp/4484479',
 'https://www.amazon.it/dp/4484479',
 'https://www.amazon.de/dp/4484568',
 'https://www.amazon.fr/dp/4484568',
 'https://www.amazon.de/dp/4484576',
 'https://www.amazon.fr/dp/4484576',
 'https://www.amazon.de/dp/4484584',
 'https://www.amazon.fr/dp/4484584',
 'https://www.amazon.fr/dp/4484592',
 'https://www.amazon.it/dp/4484592',
 'https://www.amazon.de/dp/4484606',
 'https://www.amazon.fr/dp/4484606',
 'https://www.amazon.de/dp/4484622',
 'https://www.amazon.fr/dp/4484622',
 'https://www.amazon.de/dp/4484649',
 'https://www.amazon.fr/dp/4484649',
 'https://www.amazon.de/dp/4484657',
 'https://www.amazon.fr/dp/4484657',
 'https://www.amazon.de/dp/4484665',
 'https://www.amazon.fr/dp/4484665',
 'https://www.amazon.de/dp/4484681',
 'https://www.amazon.fr/dp/4484681',
 'https://www.amazon.de/dp/4484894',
 'https://www.amazon.fr/dp/4484894',
 'https://www.amazon.de/dp/4484924',
 'https://www.amazon.fr/dp/4484924',
 'https://www.amazon.de/dp/4485742',
 'https://www.amazon.fr/dp/4485742',
 'https://www.amazon.de/dp/4486072',
 'https://www.amazon.fr/dp/4486072']

    prevTime = datetime.now()
    scraped = 1


    def parse(self,response):
        # instance of ScraperItem from items.py for json file storage
        details = ScraperItem()

        extractedData = []
        
        if self.scraped % 100 == 0:
            currTime = datetime.now()
            duration = currTime - self.prevTime

            with open('timeTaken.txt', 'a') as file:
                file.write(f'{self.scraped and self.scraped - 100}-{self.scraped}, duration -> {duration} \n')

            self.prevTime = datetime.now()
        
        self.scraped += 1
        
        if response.status == 404:
            print(response.request.url)
        else:
            title = response.css('span#productTitle::text').extract_first()
            price = response.css('span.a-color-price::text').extract_first()
            img_url = response.css('div#img-canvas img::attr(src)').extract_first()
            get_details = response.xpath("//span[@class='a-list-item']/span[2]/text()".strip()).extract()
            data = {
                'title':title,
                'price':price,
                'img_url':img_url,
                'get_details':get_details
            }

            yield data
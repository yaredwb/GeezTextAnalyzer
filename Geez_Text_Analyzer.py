import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image

st.title('የፊደል ዝርያ ቆጣሪ')

st.markdown('''በግዕዝ ፊደላት የተጻፈ ማንኛዉም ጽሑፍ ላይ ሣድስ ፊደላት አብዛኛዉን ጊዜ ከሌሎች የፊደል ዝርያዎች ቁጥራቸዉ በዛ ብሎ ይገኛል ይባላል። ይህንን እዚህ በተግባር መፈተሽ ይቻላል። የምሳሌ ጽሑፉ [ከዊኪፔዲያ](https://am.wikipedia.org/wiki/ሪቻርድ_ፋይንማን) የተወሰደ ሲሆን በሌላ ማንኛውም ርዝመት ያለው ጽሑፍ መቀየር ይቻላል።''')

text = st.text_area(
  label='ምሳሌ ጽሑፍ',
  height=300,
  value='''ሪቻርድ ፋይንማን (1910-1980) የ20ኛው ክፍለ ዘመን እውቅ የተፈጥሮ ህግጋት መርማሪ ነበር። የተወለደውም እዚያው አሜሪካ፣ ኩዊንስ እተባለ ከተማ፣ ኒው ዮርክ ክፍለ ሃገር ነበር። የመጀመሪያው የአቶሚክ ቦምብ ከሰሩት ሰዎች መካከል አንዱ ነበር። በራሱ በግሉ ባበረከታቸው የተለያዩ የጥናት ጽሑፎች ምክንያት የኖቤል ሽልማት አሸናፊም የነበር ሰው ነው።

  ፋይንማን፣ የኳንተም ሜካኒክስን የእውቀት ዘርፍ ካዳበሩት ቀደምት ተማሪወች ወገን ነው። የመንገድ ማጎሪያ (ፓዝ ኤንቴግራል) ቀመርን ለኳንተም ሥነ እንቅስቃሴ በማዋሉና፣ የኳንተም ኤሌክትሮ-እንቅስቃሴ (ኤሌክትሮ ዳይናሚክስ)ን በማጥናቱ ስለዚህም ስራው ከሌሎች ሁለት ሳይንቲስቶች ጋር የኖቬል ሽልማት በ1957ዓ.ም. ተሸልሟል። የሂሳብ ቀመሮችንም አቅልሎ ለማሳየት የሚጠቅም የፋይናማን ምስል የተባለውን ዘዴም በመቀየሱ ስሙ ይጠራል፡፡

  ፋይንማን፣ ከኳንትም ሜካኒክስ ውጭ የናኖ ቴክኖሎጂን፣ ኳንትም ስሌትን በመጀመር ይጠቀሳል። በተረፈም የመንኮራኩሯ ስፔስ ሸትል ቻሌንጀርን በአየር ላይ መጋየት ከመረመሩት ሰዎች አንዱ ነበር።

  ከዚህ በተረፈ የሥነ ተፈጥሮ (ፊዚክስ) ትምህርትን ለሰፊው ህብረተሰብ ለማካፈል ባደረገው ጥረቱ ስሙ ይነሳል። ለዚህ ተግባሩ የደረሳቸው መጻህፍቱ ታዋቂዎች ነበሩ።'''
)

fideloch = [char for char in text if char != " "]

geez = 'ሀለሐመሠረሰሸቀቐበቨተቸኀነኘአከኸወዐዘዠየደዸጀገጘጠጨጰጸፀፈፐ'
kabe = 'ሁሉሑሙሡሩሱሹቁቑቡቩቱቹኁኑኙኡኩኹዉዑዙዡዩዱዹጁጉጙጡጩጱጹፁፉፑ'
sals = 'ሂሊሒሚሢሪሲሺቂቒቢቪቲቺኂኒኚኢኪኺዊዒዚዢዪዲዺጂጊጚጢጪጲጺፂፊፒ'
rabe = 'ሃላሓማሣራሳሻቃቓባቫታቻኃናኛኣካኻዋዓዛዣያዳዻጃጋጛጣጫጳጻፃፋፓ'
hams = 'ሄሌሔሜሤሬሴሼቄቔቤቬቴቼኄኔኜኤኬኼዌዔዜዤዬዴዼጄጌጜጤጬጴጼፄፌፔ'
sads = 'ህልሕምሥርስሽቅቕብቭትችኅንኝእክዅዕዝዥይድዽጅግጝጥጭጵጽፅፍፕ'
sabe = 'ሆሎሖሞሦሮሶሾቆቖቦቮቶቾኆኖኞኦኮኾዎዖዞዦዮዶዾጆጎጞጦጮጶጾፆፎፖ'
special = 'ሏሗሟሧሯሷሿቇቧቯቷቿኇኗኟኧኯዟዧዯዷዿጇጏጟጧጯጷጿፇፏፗቈቊቋቌቍቘቚቛቜቝኈኊኋኌኍኰኲኳኴኵዀዂዃዄዅጐጒጓጔጕፘፙፚ'
punctuation = '፡።፣፤፥፦፧፨'
numbers = '፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼0123456789'
latin = 'abcdefghijklmnopqrstuvwxyz,.;:[]{-+*#@$%^&()_"?`~|'

zer = np.array(['ግዕዝ', 'ካዕብ', 'ሣልስ', 'ራብዕ', 'ሓምስ', 'ሣድስ', 'ሳብዕ', 'ልዩ ዝርያ', 'ሥርዓተ ነጥብ', 'ቁጥር', 'ሌላ'])
counts = np.zeros(11)
other = 0

z1, z2, z3, z4, z5, z6, z7 = [], [], [], [], [], [], []
liyu, netib, qutr, lela = [], [], [], []

for fidel in fideloch:
  if fidel in geez:
    counts[0] += 1
    z1.append(fidel)
  elif fidel in kabe:
    counts[1] += 1
    z2.append(fidel)
  elif fidel in sals:
    counts[2] += 1
    z3.append(fidel)
  elif fidel in rabe:
    counts[3] += 1
    z4.append(fidel)
  elif fidel in hams:
    counts[4] += 1
    z5.append(fidel)
  elif fidel in sads:
    counts[5] += 1
    z6.append(fidel)
  elif fidel in sabe:
    counts[6] += 1
    z7.append(fidel)
  elif fidel in special:
    counts[7] += 1
    liyu.append(fidel)
  elif fidel in punctuation:
    counts[8] += 1
    netib.append(fidel)
  elif fidel in numbers:
    counts[9] += 1
    qutr.append(fidel)
  elif fidel in latin:
    counts[10] += 1
    lela.append(fidel)
  else:
    other += 1

data = np.hstack((zer[:,None], counts[:,None]))
data = pd.DataFrame(data, columns=['ዝርያ', 'ብዛት'])
data['ብዛት'] = data['ብዛት'].apply(lambda x: int(float(x)))

copy = data.copy()
copy.set_index('ዝርያ', inplace=True)
st.write(copy.T, index=False)

fig = px.bar(data.head(7), x='ዝርያ', y='ብዛት')
st.write(fig)

options = []
zeroch = []
types = [z1, z2, z3, z4, z5, z6, z7, liyu, netib, qutr, lela]
for i, t in enumerate(types):
  if len(t) > 0:
    options.append(zer[i])
    zeroch.append(types[i])

if st.checkbox('ከምሳሌ ጽሑፉ ውስጥ እያንዳንዱን የፊደል ዝርያ ወይም ምልክት ለማየት', value=False):
  m = st.selectbox('ዝርያ', (options))
  index = options.index(m)  
  st.write(zeroch[index])

st.header('እና ምን ይጠበስ?')

st.markdown('''ዓሳ በዘይት! :-) ማለቴ በጣም ቀልጣፋና በተቻለ መጠን አነስተኛ ቁጥር ያላቸዉን ቁልፎች በመጫን ለመጻፍ የሚያስችል ኪቦርድ ዲዛይን ለማድረግ ይህን ከግምት ውስጥ ማስገባት ወሳኝ ነው። ከተደጋጋሚ ሙከራ በኋላ እንዳስተዋልኩት በርግጥም ሣድስ ፊደላት ብዙ ጊዜ አብዛኛውን ቁጥር የሚይዙ ሲሆን የግዕዝ ዝርያ ፊደላት ደግሞ ብዙ ጊዜ በሁለተኛ ደረጃ ላይ ይመጣሉ። ምናልባትም በሣድስ እና በግዕዝ ፊደላት ላይ ደግሞ ተጨማሪ ምርመራ በማድረግና የትኞቹ ፊደላት በብዛት እንደሚያጋጥሙ በማየት ሁለቱንም ያመዛዘነ በጣም ቀልጣፋ ኪቦርድ መስራት የሚቻል ይመስለኛል። ሞባይል ላይ እስካሁን ከተጠቀምኩባቸው ኪቦርዶች `አገርኛ Compact` በሣድስ ላይ የተመሰረተና (ከአገርኛ ሌሎች አቀማመጦች በተጨማሪ) ለመጠቀም ቀላል የሆነ ኪቦርድ አለው። በሌላ በኩል የ`Microsoft Swiftkey Amharic` ኪቦርድ በዋናነት በግዕዝ ዝርያዎች ላይ የተመሰረተ ነው። በቅርቡ ከግዕዝ እና ከሣድስ ዝርያዎች የትኞቹ ፊደላት በብዛት እንደሚያጋጥሙ ለማሳየት እሞክራለሁ።
  ''')

image = Image.open('images/amharic_keyboards.png')
st.image(image, caption='የ\'Microsoft Swiftkey Amharic\' እና የ\'አገርኛ Compact\' ኪቦርዶች አቀማመጥ', use_column_width=True)

st.write(' ')
st.write(' ')

st.markdown(  
  '''
  Made by Yared: 
  [GitHub](https://github.com/yaredwb) [LinkedIn](https://www.linkedin.com/in/yaredworku/) [Twitter](https://twitter.com/yaredwb) [Personal Website](https://yaredwb.com/)
  '''
)
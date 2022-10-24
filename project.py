from numpy import sort
import pandas as pd
import plotly
import streamlit as st
import plotly.graph_objects as go
import altair as alt

#Read Data CSV
dflayoff = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSU-Uzxan4cQhXjmRSMpbaxqP_l9I1dnMPOxxHkeiG2m89I4LtXkLmmxGkgtZIbW8GLTmFQ-V8ovt6K/pub?output=csv")
dflayoff['Bulan'] = pd.to_datetime(dflayoff['Bulan'])

#LAY-OFF EMPLOYEE STARTUP
st.title("LAY-OFF EMPLOYEE STARTUP")

st.markdown(
"""
Kata Startup adalah berasal dari serapan dari Bahasa Inggris yang berarti bisnis yang baru saja dirintis atau bisnis rintisan. Startup adalah perusahaan rintisan yang belum lama beroperasi. Dengan kata lain, startup artinya perusahaan yang baru masuk atau masih berada pada fase pengembangan atau penelitian untuk terus menemukan pasar maupun mengembangkan produknya. \n \n
Menurut data (layoffs.fyi), jumlah layoff (PHK) karyawan saat ini sedang mengalami pengingkatan pada beberapa perusahaan startup. Meskipun berbagai stimulus dan bantuan diberikan kepada para pengusaha agar sebisa mungkin untuk tidak melakukan Pemutusan Hubungan Kerja (PHK) atau layoff, namun tidak dapat dipungkiri bahwa pada akhirnya layoff merupakan satu-satunya jalan yang dapat diambil perusahaan startup.
\n
Total (yang terkonfirmasi) employee yang terkena layoff mencapai lebih dari 187 ribu sejak era covid-19 (layoffs.fyi). Namun seperti yang kita ketahui, Covid-19 sendiri mengalami penurunan secara konsisten pada akhir Februari 2022 (https://covid19.go.id/). Hal ini dapat disimpulkan bahwa Layoff dengan sebab covid-19 berakhir pada Februari 2022 dan pada tahun yang sama dimulai kembali gelombang besar startup employee layoff yang digadang gadang disebabkan oleh dimulainya era Tech Winter. 
Berikut data gelombang besar Layoff startup :
"""
)


#PLOT DATA LAY-OFF DALAM KURUN WAKTU KEDALAM BAR CHART
st.write("Dua gelombang besar Layoff startup")
#ada pada saat Covid 19 dan Tech Winter 2022
laidoff = dflayoff[['Bulan', 'Jumlah Tiap bulan']].set_index('Bulan').resample('M').sum()
st.line_chart(laidoff)

col1, col2 = st.columns(2)
with col1:
   st.caption("Layoff Masa Covid-19 (Maret 2020 - Februari 2022)")

with col2:
   st.caption("Layoff Masa Tech Winter 2022 (Maret 2022 - Oktober 2022)")
st.text("")

st.markdown(
"""
Tech Winter bisa kita artikan sebagai periode penuruan ketertarikan dan investasi dalam bidang teknologi maju (advanced technology). Seperti yang kita ketahui, baru-baru ini terjadi downturn trend tech-based startup yang membuat kita semakin merasakan adanya tech winter(calcalistech). Tidak hanya di Indonesia, namun juga di seluruh dunia. Beberapa issue yang baru-baru ini terjadi : 
- Banyaknya Layoff dari Startup di Dunia dan Indonesia
- Penjualan Ecommerce menurun hingga 20% pada campaign 10.10 2022
- Fabelio dinyatakan pailit
- Traveloka menutup layanan Eats, Send dan Mart
- HappyFresh menghentikan operasionalnya
- dan lain sebagainya\n\n

\nPerkembangan teknologi, aliran pendanaan, sumber daya manusia dan ekosistem startup berbeda di setiap Negara. Hal tersebut mempengaruhi perkembangan start-up di setiap negara, United States merupakan negara yang paling maju dalam bidang startup tech-based, Perusahaan besar seperti Tesla, Microsoft, Facebook (Meta), Netflix dan lain sebagainya berpusat disana. Jadi tidak heran jika duniamengalami dampak tech winter, United States menjadi negara yang paling banyak melakukan Layoff.\n

"""
)

#PLOT DATA LAYOFF TIAP NEGARA KEDALAM PIE CHART
fig = go.Figure(
    go.Pie(
    labels = dflayoff['Negara'],
    values = dflayoff['Jumlah Tiap Negara'],
    hoverinfo = "label+percent",
    textinfo = "value"
))
st.write("Lay off Employee startup di beberapa Negara")
st.plotly_chart(fig)

#st.dataframe(df) 

#SEKTOR INDUSTRI YANG PALING TERDAMPAK
st.markdown("***")
st.header("Sektor Industri yang Paling Terdampak")
st.write("Jumlah bidang industri yang paling banyak melakukan layoff (bukan jumlah karyawan layoff) adalah Finance atau biasa disebut fintech. Bidang Finace merupakan yang paling banyak melakukan layoff karyawannya, sebetulnya hal ini sudah diprediksikan sejak beberapa tahun sebelumnya karena pada bidang industri ini persaingan semakin ketat. Sudah ada beberapa cara yang dilakukan oleh fintech untuk bersaing, mulai dari menurunkan bunga, memperbesar anggaran marketing, bekerjasama dengan perusahaan bidang lain seperti retail atau bahkan memperlebar bisnis hingga membuat retail/marketplace yang didasari oleh fintech itu sendiri. ")

# PLOT DATA SEKTOR INDUSTRI KEDALAM BAR CHART
st.write("Sektor Industri terdampak ")
industri = dflayoff[['Jumlah Tiap industri', 'Industri']]
bar_chart = alt.Chart(industri).mark_bar().encode(
    x="Jumlah Tiap industri:Q",
    y=alt.Y("Industri:N", sort="-x")
    )
st.altair_chart(bar_chart, use_container_width=True)

#PERUBAHAN YANG TERJADI DARI FENOMENA INI
st.markdown("***")
st.header("Perubahan Yang Terjadi Dari Fenomena Ini")
col1, col2 = st.columns(2)
with col1:
   st.markdown(
      """
      1. Perusahaan berbasis teknologi sedang menjalani periode sulit dalam dekade ini, rata-rata perusahaan unicorn yang lahir (startup dengan valuasi lebih dari 1B USD) turun 80% dari tahun lalu (Crunchbase). Layoff atau PHK juga meningkat, dengan lebih dari 85.000 (era techwinter) karyawan yang dihentikan dari pekerjaaanya diseluruh dunia (berdasarkan Layoff.fyi)
      2. Meskipun ulasan bahwa investasi semakin menipis, sebagian besar investor global masih melakukan rata-rata 20 hingga 30 transaksi menurut analisa dari SVB (Sillicon Valley Bank). Bahkan ada yang bilang bahwa 2022 merupakan tahun kedua yang terbaik untuk investasi dalam sektor Tech-based Startup karena harga dasar sedang dalam kondisi rendah.
      """
      )
with col2:
   st.markdown(
      """
      3. Pada siklus Layoff kali ini dan penuruan trend terhadap perusahaan tech-base terjadi pada perusahaan-perusahaan yang tidak memiliki produk yang pasti atau bisnis model yang jelas untuk berlomba dalam mengejar profit. Penurunan tech-based startup ini bukanlah penurunan secara permanen, namun sebuah siklus perbaikan yang terjadi pada indusri yang seharusnya terjadi pada tahun-tahun yang lalu.
      4. Untuk pertamakalinya, akses mudah untuk pendanaan sudah tidak tersedia lagi. Investor menjadi lebih selektif terhadap portofolio dan para Founders Startup harus menyesuaikan dengan hal ini.Sementara hal-hal seperti valuasi menjadi lebih konservatif dan permintaan untuk pendanaan dengan hutang untuk memperkuat keuangan terhadap market di 2023 menjadi perhatian, Industri ini akan tetap kuat.
      """
   )   

#REFERENCES
st.markdown("***")
st.header("References")
st.markdown(
"""
- https://layoffs.fyi/
- https://simplicable.com/new/technology-winter
- https://www.bloomberg.com/news/newsletters/2020-04-01/startups-keep-slashing-jobs@Eccomurz
- https://www.cnbcindonesia.com/tech/20220930152639-37-376315/baru-dapat-rp-45-triliun-traveloka-tutup-eats-dan-send
- https://www.svb.com/trends-insights/reports/state-of-saas-report
- https://www.jawapos.com/ekonomi/finance/06/02/2020/kemunculan-fintech-bikin-persaingan-antarbank-makin-ketat/
- https://covid19.go.id/
- https://www.calcalistech.com/ctechnews/article/ef8n3y5i1
- https://katadata.co.id/yuliawati/digital/5e9a4e6b92155/persaingan-bisnis-dompet-digital-makin-ketat-dan-mengerucut
- https://investor.id/finance/238203/persaingan-ketat-tren-tingkat-bunga-fintech-lending-mulai-menuru
"""
)

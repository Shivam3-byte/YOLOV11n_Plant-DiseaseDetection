"""Disease → remedy mapping for all 38 PlantVillage classes."""

REMEDIES = {
    # Apple
    "Apple___Apple_scab": {
        "plant": "Apple",
        "disease": "Apple Scab",
        "status": "diseased",
        "remedy": (
            "**Apple Scab Treatment:**\n"
            "• Apply fungicides containing captan or myclobutanil at bud break.\n"
            "• Remove and destroy fallen leaves to reduce fungal spores.\n"
            "• Prune trees to improve air circulation.\n"
            "• Use resistant apple varieties when replanting.\n"
            "• Apply copper-based sprays during dormant season."
        ),
    },
    "Apple___Black_rot": {
        "plant": "Apple",
        "disease": "Black Rot",
        "status": "diseased",
        "remedy": (
            "**Apple Black Rot Treatment:**\n"
            "• Remove mummified fruits and cankers from the tree.\n"
            "• Apply fungicides (captan, mancozeb) from pink through cover sprays.\n"
            "• Prune out dead or diseased wood 6 inches below visible infection.\n"
            "• Maintain tree vigor through proper fertilization.\n"
            "• Avoid wounding bark during cultivation."
        ),
    },
    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "disease": "Cedar Apple Rust",
        "status": "diseased",
        "remedy": (
            "**Cedar Apple Rust Treatment:**\n"
            "• Apply fungicides (myclobutanil, propiconazole) at pink stage.\n"
            "• Remove nearby eastern red cedar or juniper trees if possible.\n"
            "• Plant rust-resistant apple varieties.\n"
            "• Repeat fungicide applications every 7–10 days during wet weather.\n"
            "• Remove galls from cedar trees in late winter before they mature."
        ),
    },
    "Apple___healthy": {
        "plant": "Apple",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Apple Tree — Maintenance Tips:**\n"
            "• Continue regular pruning for good air circulation.\n"
            "• Apply balanced NPK fertilizer in early spring.\n"
            "• Monitor regularly for early signs of pests or disease.\n"
            "• Maintain proper irrigation — avoid waterlogging.\n"
            "• Mulch around the base to retain moisture."
        ),
    },
    # Blueberry
    "Blueberry___healthy": {
        "plant": "Blueberry",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Blueberry — Maintenance Tips:**\n"
            "• Maintain soil pH between 4.5–5.5 for optimal growth.\n"
            "• Apply acidifying fertilizer (ammonium sulfate) each spring.\n"
            "• Mulch with pine needles or wood chips to retain moisture.\n"
            "• Prune older canes every few years to encourage new growth.\n"
            "• Ensure adequate irrigation during fruit development."
        ),
    },
    # Cherry
    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry",
        "disease": "Powdery Mildew",
        "status": "diseased",
        "remedy": (
            "**Cherry Powdery Mildew Treatment:**\n"
            "• Apply sulfur-based or potassium bicarbonate fungicides.\n"
            "• Remove and destroy infected shoots and leaves.\n"
            "• Improve air circulation through proper pruning.\n"
            "• Avoid excessive nitrogen fertilization which promotes lush growth.\n"
            "• Apply neem oil spray as an organic alternative."
        ),
    },
    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Cherry Tree — Maintenance Tips:**\n"
            "• Prune in late summer to reduce disease risk.\n"
            "• Apply a balanced fertilizer in early spring.\n"
            "• Ensure well-drained soil to prevent root rot.\n"
            "• Monitor for aphids, cherry fruit fly, and other pests.\n"
            "• Water at the base to keep foliage dry."
        ),
    },
    # Corn (Maize)
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn (Maize)",
        "disease": "Cercospora Leaf Spot / Gray Leaf Spot",
        "status": "diseased",
        "remedy": (
            "**Corn Gray Leaf Spot Treatment:**\n"
            "• Plant resistant hybrids when available.\n"
            "• Apply foliar fungicides (strobilurin or triazole-based) at early tassel stage.\n"
            "• Rotate crops — avoid continuous corn planting.\n"
            "• Till infected crop residue to reduce inoculum.\n"
            "• Ensure good air circulation with proper plant spacing."
        ),
    },
    "Corn_(maize)___Common_rust_": {
        "plant": "Corn (Maize)",
        "disease": "Common Rust",
        "status": "diseased",
        "remedy": (
            "**Corn Common Rust Treatment:**\n"
            "• Plant rust-resistant hybrid varieties.\n"
            "• Apply fungicides (mancozeb, propiconazole) at first sign of infection.\n"
            "• Scout fields regularly, especially during cool humid weather.\n"
            "• Avoid late planting which increases exposure to rust spores.\n"
            "• Ensure balanced potassium levels to improve plant resistance."
        ),
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)",
        "disease": "Northern Leaf Blight",
        "status": "diseased",
        "remedy": (
            "**Corn Northern Leaf Blight Treatment:**\n"
            "• Apply fungicides (azoxystrobin, propiconazole) at VT/R1 stage.\n"
            "• Use resistant hybrids — check local extension recommendations.\n"
            "• Practice crop rotation with non-host crops.\n"
            "• Till crop debris to reduce overwintering spores.\n"
            "• Avoid overhead irrigation to limit leaf wetness."
        ),
    },
    "Corn_(maize)___healthy": {
        "plant": "Corn (Maize)",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Corn — Maintenance Tips:**\n"
            "• Apply nitrogen fertilizer in split doses for best uptake.\n"
            "• Ensure adequate soil moisture especially during pollination.\n"
            "• Scout for stem borers, armyworms, and aphids regularly.\n"
            "• Maintain proper plant density (60,000–80,000 plants/ha).\n"
            "• Test soil pH and keep between 5.8–7.0."
        ),
    },
    # Grape
    "Grape___Black_rot": {
        "plant": "Grape",
        "disease": "Black Rot",
        "status": "diseased",
        "remedy": (
            "**Grape Black Rot Treatment:**\n"
            "• Apply fungicides (myclobutanil, mancozeb) from budbreak through veraison.\n"
            "• Remove mummified berries and infected leaves promptly.\n"
            "• Prune to open canopy and improve air circulation.\n"
            "• Train vines to keep fruit off the ground.\n"
            "• Avoid overhead irrigation; use drip irrigation."
        ),
    },
    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape",
        "disease": "Esca (Black Measles)",
        "status": "diseased",
        "remedy": (
            "**Grape Esca Treatment:**\n"
            "• No curative chemical treatment is available.\n"
            "• Remove and destroy severely infected vines.\n"
            "• Apply wound sealant paste to pruning cuts to prevent infection.\n"
            "• Avoid pruning during wet weather.\n"
            "• Consider sodium arsenite trunk injection where legally permitted."
        ),
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape",
        "disease": "Leaf Blight (Isariopsis Leaf Spot)",
        "status": "diseased",
        "remedy": (
            "**Grape Leaf Blight Treatment:**\n"
            "• Apply copper-based fungicides or mancozeb at first symptoms.\n"
            "• Remove and destroy infected leaves and shoots.\n"
            "• Improve canopy management for better airflow.\n"
            "• Avoid excessive irrigation and waterlogging.\n"
            "• Apply protective fungicides before rainy periods."
        ),
    },
    "Grape___healthy": {
        "plant": "Grape",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Grape Vine — Maintenance Tips:**\n"
            "• Prune annually to maintain vine structure and fruit quality.\n"
            "• Apply balanced fertilizer in early spring.\n"
            "• Monitor for downy/powdery mildew and botrytis regularly.\n"
            "• Ensure good drainage to prevent root diseases.\n"
            "• Use drip irrigation to keep foliage dry."
        ),
    },
    # Orange
    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange",
        "disease": "Huanglongbing (Citrus Greening)",
        "status": "diseased",
        "remedy": (
            "**Citrus Greening (HLB) Management:**\n"
            "• No cure exists — infected trees must be removed and destroyed.\n"
            "• Control Asian citrus psyllid vector with insecticides (imidacloprid).\n"
            "• Use certified disease-free planting material.\n"
            "• Apply thermotherapy (hot water treatment) to budwood.\n"
            "• Regular grove scouting and immediate removal of symptomatic trees."
        ),
    },
    # Peach
    "Peach___Bacterial_spot": {
        "plant": "Peach",
        "disease": "Bacterial Spot",
        "status": "diseased",
        "remedy": (
            "**Peach Bacterial Spot Treatment:**\n"
            "• Apply copper-based bactericides during the growing season.\n"
            "• Plant resistant varieties (e.g., Redhaven, Reliance).\n"
            "• Avoid overhead irrigation; use drip systems.\n"
            "• Prune to improve air circulation and light penetration.\n"
            "• Apply dormant copper sprays before budbreak."
        ),
    },
    "Peach___healthy": {
        "plant": "Peach",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Peach Tree — Maintenance Tips:**\n"
            "• Apply balanced NPK fertilizer in late winter/early spring.\n"
            "• Thin fruits to 15–20 cm apart for better size and quality.\n"
            "• Prune annually for an open-center shape.\n"
            "• Monitor for peach leaf curl, brown rot, and borers.\n"
            "• Irrigate regularly but avoid waterlogging."
        ),
    },
    # Pepper
    "Pepper,_bell___Bacterial_spot": {
        "plant": "Pepper (Bell)",
        "disease": "Bacterial Spot",
        "status": "diseased",
        "remedy": (
            "**Pepper Bacterial Spot Treatment:**\n"
            "• Apply copper-based bactericides at first sign of disease.\n"
            "• Use disease-free certified seed and transplants.\n"
            "• Rotate crops — avoid planting peppers in the same field annually.\n"
            "• Avoid working in fields when plants are wet.\n"
            "• Remove and destroy severely infected plant material."
        ),
    },
    "Pepper,_bell___healthy": {
        "plant": "Pepper (Bell)",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Bell Pepper — Maintenance Tips:**\n"
            "• Maintain soil pH between 6.0–6.8.\n"
            "• Apply calcium-rich fertilizer to prevent blossom end rot.\n"
            "• Stake plants to support heavy fruit loads.\n"
            "• Water consistently to avoid fruit cracking.\n"
            "• Monitor for aphids, thrips, and whiteflies regularly."
        ),
    },
    # Potato
    "Potato___Early_blight": {
        "plant": "Potato",
        "disease": "Early Blight",
        "status": "diseased",
        "remedy": (
            "**Potato Early Blight Treatment:**\n"
            "• Apply fungicides (chlorothalonil, mancozeb) at first symptoms.\n"
            "• Rotate crops with non-solanaceous crops for 2–3 years.\n"
            "• Plant certified disease-free seed potatoes.\n"
            "• Remove and destroy infected foliage promptly.\n"
            "• Ensure adequate potassium nutrition to improve resistance."
        ),
    },
    "Potato___Late_blight": {
        "plant": "Potato",
        "disease": "Late Blight",
        "status": "diseased",
        "remedy": (
            "**Potato Late Blight Treatment:**\n"
            "• Apply fungicides (metalaxyl, cymoxanil, chlorothalonil) preventively.\n"
            "• Destroy infected plant material — do NOT compost.\n"
            "• Hilling soil around plants reduces tuber infection.\n"
            "• Use blight-resistant varieties (e.g., Sarpo Mira, Defender).\n"
            "• Monitor weather forecasts and apply fungicides before rain."
        ),
    },
    "Potato___healthy": {
        "plant": "Potato",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Potato — Maintenance Tips:**\n"
            "• Apply balanced NPK fertilizer based on soil test results.\n"
            "• Hill soil around plants to prevent greening of tubers.\n"
            "• Irrigate consistently — avoid wet/dry cycles.\n"
            "• Scout for Colorado potato beetle and aphids.\n"
            "• Harvest when vines die back naturally for best storage."
        ),
    },
    # Raspberry
    "Raspberry___healthy": {
        "plant": "Raspberry",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Raspberry — Maintenance Tips:**\n"
            "• Prune out old canes (floricanes) after fruiting.\n"
            "• Apply balanced fertilizer in early spring.\n"
            "• Maintain soil pH between 5.5–6.5.\n"
            "• Provide support structures (trellis) for canes.\n"
            "• Monitor for cane borers and raspberry aphids."
        ),
    },
    # Soybean
    "Soybean___healthy": {
        "plant": "Soybean",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Soybean — Maintenance Tips:**\n"
            "• Use rhizobium inoculant on seed for nitrogen fixation.\n"
            "• Rotate with corn or small grains to reduce diseases.\n"
            "• Scout regularly for soybean aphids and spider mites.\n"
            "• Maintain soil pH between 6.0–7.0.\n"
            "• Apply potassium and phosphorus based on soil tests."
        ),
    },
    # Squash
    "Squash___Powdery_mildew": {
        "plant": "Squash",
        "disease": "Powdery Mildew",
        "status": "diseased",
        "remedy": (
            "**Squash Powdery Mildew Treatment:**\n"
            "• Apply neem oil, potassium bicarbonate, or sulfur sprays.\n"
            "• Remove heavily infected leaves to slow spread.\n"
            "• Improve air circulation with proper plant spacing.\n"
            "• Avoid overhead irrigation and water in the morning.\n"
            "• Plant resistant varieties when available."
        ),
    },
    # Strawberry
    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "disease": "Leaf Scorch",
        "status": "diseased",
        "remedy": (
            "**Strawberry Leaf Scorch Treatment:**\n"
            "• Apply fungicides (captan, thiram) at planting and in early spring.\n"
            "• Remove and destroy infected leaves after harvest.\n"
            "• Plant certified disease-free runners.\n"
            "• Renovate plantings by mowing and thinning after harvest.\n"
            "• Avoid overhead irrigation; use drip systems."
        ),
    },
    "Strawberry___healthy": {
        "plant": "Strawberry",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Strawberry — Maintenance Tips:**\n"
            "• Mulch with straw to keep fruit clean and reduce moisture loss.\n"
            "• Apply balanced fertilizer after harvest.\n"
            "• Remove runners to direct energy to mother plants.\n"
            "• Monitor for spider mites, gray mold, and slugs.\n"
            "• Replace plantings every 3–4 years for best yields."
        ),
    },
    # Tomato
    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "disease": "Bacterial Spot",
        "status": "diseased",
        "remedy": (
            "**Tomato Bacterial Spot Treatment:**\n"
            "• Apply copper-based bactericides + mancozeb combination sprays.\n"
            "• Use disease-free certified seed or transplants.\n"
            "• Rotate crops — avoid planting tomatoes in the same spot annually.\n"
            "• Stake and prune for better air circulation.\n"
            "• Avoid working with plants when foliage is wet."
        ),
    },
    "Tomato___Early_blight": {
        "plant": "Tomato",
        "disease": "Early Blight",
        "status": "diseased",
        "remedy": (
            "**Tomato Early Blight Treatment:**\n"
            "• Apply fungicides (chlorothalonil, mancozeb, azoxystrobin).\n"
            "• Remove lower infected leaves and avoid splashing soil on foliage.\n"
            "• Mulch around plants to reduce soil splash.\n"
            "• Rotate crops with non-solanaceous plants for 2 years.\n"
            "• Ensure adequate potassium nutrition for better resistance."
        ),
    },
    "Tomato___Late_blight": {
        "plant": "Tomato",
        "disease": "Late Blight",
        "status": "diseased",
        "remedy": (
            "**Tomato Late Blight Treatment:**\n"
            "• Apply fungicides (metalaxyl, chlorothalonil) preventively.\n"
            "• Remove and destroy infected plants immediately — do NOT compost.\n"
            "• Avoid overhead irrigation; water at the base.\n"
            "• Use resistant varieties (e.g., Mountain Magic, Jasper).\n"
            "• Apply copper-based sprays as a protective measure."
        ),
    },
    "Tomato___Leaf_Mold": {
        "plant": "Tomato",
        "disease": "Leaf Mold",
        "status": "diseased",
        "remedy": (
            "**Tomato Leaf Mold Treatment:**\n"
            "• Reduce humidity by improving ventilation in greenhouses.\n"
            "• Apply fungicides (chlorothalonil, mancozeb, copper).\n"
            "• Remove and destroy infected leaves promptly.\n"
            "• Avoid overhead irrigation; use drip systems.\n"
            "• Plant resistant varieties where available."
        ),
    },
    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato",
        "disease": "Septoria Leaf Spot",
        "status": "diseased",
        "remedy": (
            "**Tomato Septoria Leaf Spot Treatment:**\n"
            "• Apply fungicides (chlorothalonil, mancozeb, copper) at first sign.\n"
            "• Remove infected lower leaves immediately.\n"
            "• Mulch to prevent soil splash onto leaves.\n"
            "• Rotate crops with non-solanaceous plants.\n"
            "• Stake plants to improve air circulation."
        ),
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato",
        "disease": "Spider Mites (Two-spotted)",
        "status": "diseased",
        "remedy": (
            "**Tomato Spider Mite Treatment:**\n"
            "• Apply miticides (abamectin, bifenazate) or insecticidal soap.\n"
            "• Spray undersides of leaves where mites congregate.\n"
            "• Introduce predatory mites (Phytoseiulus persimilis) for biological control.\n"
            "• Maintain adequate irrigation — drought stress worsens infestations.\n"
            "• Use neem oil spray as an organic alternative."
        ),
    },
    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "disease": "Target Spot",
        "status": "diseased",
        "remedy": (
            "**Tomato Target Spot Treatment:**\n"
            "• Apply fungicides (azoxystrobin, chlorothalonil, mancozeb).\n"
            "• Remove and destroy infected leaves and plant debris.\n"
            "• Improve air circulation through staking and pruning.\n"
            "• Avoid overhead irrigation.\n"
            "• Rotate crops to reduce soilborne inoculum."
        ),
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato",
        "disease": "Yellow Leaf Curl Virus",
        "status": "diseased",
        "remedy": (
            "**Tomato Yellow Leaf Curl Virus Management:**\n"
            "• Control whitefly vectors with insecticides (imidacloprid, thiamethoxam).\n"
            "• Use yellow sticky traps to monitor and reduce whitefly populations.\n"
            "• Plant resistant/tolerant varieties (e.g., Ty-1 gene varieties).\n"
            "• Use reflective mulches to repel whiteflies.\n"
            "• Remove and destroy infected plants immediately to reduce virus spread."
        ),
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato",
        "disease": "Tomato Mosaic Virus",
        "status": "diseased",
        "remedy": (
            "**Tomato Mosaic Virus Management:**\n"
            "• No chemical cure available — use virus-free certified seed.\n"
            "• Wash hands and disinfect tools before handling plants.\n"
            "• Remove and destroy infected plants promptly.\n"
            "• Control aphid vectors with insecticides or reflective mulches.\n"
            "• Avoid tobacco use near plants — tobacco mosaic virus can cross-infect."
        ),
    },
    "Tomato___healthy": {
        "plant": "Tomato",
        "disease": "None",
        "status": "healthy",
        "remedy": (
            "**Healthy Tomato — Maintenance Tips:**\n"
            "• Stake or cage plants for support and air circulation.\n"
            "• Apply calcium nitrate to prevent blossom end rot.\n"
            "• Water consistently at the base to avoid foliar diseases.\n"
            "• Scout weekly for early blight, late blight, and pests.\n"
            "• Rotate tomatoes with non-solanaceous crops each season."
        ),
    },
}

_FALLBACK = {
    "plant": "Unknown",
    "disease": "Unknown",
    "status": "unknown",
    "remedy": (
        "**Remedy information not available.**\n"
        "Please consult your local agricultural extension officer for advice."
    ),
}


def get_remedy(class_name: str) -> dict:
    """Return remedy info for a PlantVillage class name, with fallback."""
    return REMEDIES.get(class_name, _FALLBACK)

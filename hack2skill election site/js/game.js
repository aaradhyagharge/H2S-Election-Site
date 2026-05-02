// ============================================================
// MATDAN — Election Mystery Game Logic (game.js)
// ============================================================

const gameData = [
    {
        chapter: 1,
        title: "Mystery of the Village",
        image: "🏮",
        text: {
            en: "You arrive in Rampur. A group of villagers is gathered near the banyan tree. They look worried. 'Don't go to the booth,' one says. 'They say our votes don't matter and it's all fixed.'",
            hi: "आप रामपुर पहुँचते हैं। बरगद के पेड़ के पास ग्रामीणों का एक समूह इकट्ठा है। वे चिंतित लग रहे हैं। 'बूथ पर मत जाओ,' एक कहता है। 'वे कहते हैं कि हमारे वोटों से कोई फर्क नहीं पड़ता और सब पहले से तय है।'",
            mr: "तुम्ही रामपूरला पोहोचता. वडाच्या झाडाखाली गावकऱ्यांचा एक गट जमला आहे. ते काळजीत दिसत आहेत. 'बूथवर जाऊ नका,' एक म्हणतो. 'ते म्हणतात आपल्या मताने काही फरक पडत नाही आणि सर्व काही आधीच ठरलेले असते.'"
        },
        choices: [
            {
                text: { en: "Ignore them and keep walking", hi: "उन्हें अनदेखा करें और चलते रहें", mr: "त्यांच्याकडे दुर्लक्ष करा आणि चालत राहा" },
                correct: false,
                score: 50,
                feedback: {
                    en: "Ignoring misinformation doesn't stop it. As a responsible citizen, you should seek the truth.",
                    hi: "गलत सूचनाओं को अनदेखा करने से वे रुकती नहीं हैं। एक जिम्मेदार नागरिक के रूप में, आपको सच्चाई जाननी चाहिए।",
                    mr: "चुकीच्या माहितीकडे दुर्लक्ष केल्याने ती थांबत नाही. एक जबाबदार नागरिक म्हणून तुम्ही सत्य शोधले पाहिजे."
                }
            },
            {
                text: { en: "Ask them why they think so and explain the importance of voting", hi: "उनसे पूछें कि वे ऐसा क्यों सोचते हैं और मतदान के महत्व के बारे में बताएं", mr: "त्यांना असे का वाटते ते विचारा आणि मतदानाचे महत्त्व पटवून द्या" },
                correct: true,
                score: 100,
                feedback: {
                    en: "Correct! Every vote counts in our democracy. You've cleared the first hurdle of misinformation.",
                    hi: "सही! हमारे लोकतंत्र में हर वोट मायने रखता है। आपने गलत सूचना की पहली बाधा पार कर ली है।",
                    mr: "बरोबर! आपल्या लोकशाहीत प्रत्येक मत महत्त्वाचे असते. तुम्ही चुकीच्या माहितीचा पहिला अडथळा दूर केला आहे."
                }
            }
        ]
    },
    {
        chapter: 2,
        title: "EPIC Ka Raaz",
        image: "🪪",
        text: {
            en: "An elderly neighbor, Kaki, says she wants to vote but doesn't have a 'Pehchan Patra' (Voter ID). She thinks it's too late to register.",
            hi: "एक बुजुर्ग पड़ोसी, काकी कहती हैं कि वह वोट देना चाहती हैं लेकिन उनके पास 'पहचान पत्र' नहीं है। उन्हें लगता है कि पंजीकरण के लिए बहुत देर हो चुकी है।",
            mr: "एक वृद्ध शेजारी, काकी म्हणतात की त्यांना मतदान करायचे आहे पण त्यांच्याकडे 'ओळखपत्र' नाही. त्यांना वाटते की नोंदणीसाठी आता खूप उशीर झाला आहे."
        },
        choices: [
            {
                text: { en: "Tell her to use Form 6 for new registration", hi: "उन्हें नए पंजीकरण के लिए फॉर्म 6 का उपयोग करने के लिए कहें", mr: "त्यांना नवीन नोंदणीसाठी फॉर्म ६ वापरण्यास सांगा" },
                correct: true,
                score: 100,
                feedback: {
                    en: "Exactly! Form 6 is the key to entering the electoral roll. You helped Kaki get her right to vote!",
                    hi: "बिल्कुल! फॉर्म 6 मतदाता सूची में प्रवेश करने की कुंजी है। आपने काकी को अपना वोट देने का अधिकार दिलाने में मदद की!",
                    mr: "अगदी बरोबर! फॉर्म ६ ही मतदार यादीत नाव नोंदवण्याची गुरुकिल्ली आहे. तुम्ही काकींना त्यांचा मतदानाचा अधिकार मिळवून देण्यात मदत केलीत!"
                }
            },
            {
                text: { en: "Tell her she can't vote this time", hi: "उनसे कहें कि वह इस बार वोट नहीं दे सकतीं", mr: "त्यांना सांगा की त्या यावेळी मतदान करू शकत नाहीत" },
                correct: false,
                score: 0,
                feedback: {
                    en: "Wait! Registration is often open until just before the election. Never give up on a citizen's right.",
                    hi: "रुको! पंजीकरण अक्सर चुनाव से ठीक पहले तक खुला रहता है। नागरिक के अधिकार पर कभी हार न मानें।",
                    mr: "थांबा! नोंदणी अनेकदा निवडणुकीच्या अगदी आधीपर्यंत सुरू असते. नागरिकांच्या हक्काबाबत कधीही हार मानू नका."
                }
            }
        ]
    }
];

let currentSceneIndex = 0;
let totalScore = 0;
let userAvatar = 'boy';

function initGame() {
    const startBtn = document.getElementById('start-game-btn');
    const avatarOpts = document.querySelectorAll('.avatar-option');

    avatarOpts.forEach(opt => {
        opt.addEventListener('click', () => {
            avatarOpts.forEach(o => o.classList.remove('selected'));
            opt.classList.add('selected');
            userAvatar = opt.dataset.avatar;
        });
    });

    startBtn.addEventListener('click', () => {
        document.getElementById('start-screen').classList.add('hidden');
        document.getElementById('gameplay-area').classList.remove('hidden');
        renderScene();
    });

    document.getElementById('next-scene-btn').addEventListener('click', nextScene);
}

function renderScene() {
    const scene = gameData[currentSceneIndex];
    const lang = window.getCurrentLang ? window.getCurrentLang() : 'en';

    document.getElementById('scene-image').textContent = scene.image;
    document.getElementById('scene-text').textContent = scene.text[lang];
    
    // Update tracker
    document.querySelectorAll('.chapter-dot').forEach((dot, i) => {
        if (i < currentSceneIndex) dot.className = 'chapter-dot done';
        else if (i === currentSceneIndex) dot.className = 'chapter-dot active';
        else dot.className = 'chapter-dot';
    });

    const choiceContainer = document.getElementById('choice-buttons');
    choiceContainer.innerHTML = '';

    scene.choices.forEach((choice, idx) => {
        const btn = document.createElement('button');
        btn.className = 'choice-btn';
        btn.textContent = choice.text[lang];
        btn.addEventListener('click', () => handleChoice(choice, btn));
        choiceContainer.appendChild(btn);
    });

    document.getElementById('feedback-panel').classList.add('hidden');
}

async function handleChoice(choice, btn) {
    const lang = window.getCurrentLang ? window.getCurrentLang() : 'en';
    const allBtns = document.querySelectorAll('.choice-btn');
    allBtns.forEach(b => b.disabled = true);

    if (choice.correct) {
        btn.classList.add('correct');
        totalScore += choice.score;
        updateScoreDisplay();
        document.getElementById('feedback-title').textContent = (lang === 'en' ? 'Excellent!' : (lang === 'hi' ? 'उत्कृष्ट!' : 'उत्कृष्ट!'));
        document.getElementById('feedback-title').style.color = 'var(--ind-green)';
    } else {
        btn.classList.add('wrong');
        document.getElementById('feedback-title').textContent = (lang === 'en' ? 'Think again...' : (lang === 'hi' ? 'फिर से सोचें...' : 'पुन्हा विचार करा...'));
        document.getElementById('feedback-title').style.color = 'var(--deep-red)';
    }

    document.getElementById('feedback-text').textContent = choice.feedback[lang];
    document.getElementById('feedback-panel').classList.remove('hidden');
}

function updateScoreDisplay() {
    const scoreEl = document.getElementById('game-score');
    if (scoreEl) scoreEl.textContent = String(totalScore).padStart(4, '0');
}

function nextScene() {
    currentSceneIndex++;
    if (currentSceneIndex < gameData.length) {
        renderScene();
    } else {
        finishGame();
    }
}

function finishGame() {
    document.getElementById('gameplay-area').classList.add('hidden');
    document.getElementById('end-screen').classList.remove('hidden');
    document.getElementById('final-score').textContent = totalScore;
    
    // Save to DB via API
    const userId = localStorage.getItem('matdan_user_id');
    if (userId) {
        fetch('/api/game/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                user_id: userId,
                score: totalScore,
                chapter: currentSceneIndex,
                language: window.getCurrentLang()
            })
        });
    }

    // Award badges
    const badgesContainer = document.getElementById('badges-container');
    badgesContainer.innerHTML = `
        <div class="hud-card green-variant" style="padding:1rem;">
            <div style="font-size:2rem;">🎖️</div>
            <div style="font-size:0.8rem; font-weight:700;">JAGRUK NAGARIK</div>
        </div>
    `;
}

document.addEventListener('DOMContentLoaded', initGame);

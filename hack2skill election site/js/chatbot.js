// ============================================================
// MATDAN — Chatbot (chatbot.js)
// ============================================================
const API = '/api/chatbot';
let sessionId = sessionStorage.getItem('matdan_session') || ('sess_' + Date.now());
sessionStorage.setItem('matdan_session', sessionId);
let widgetOpen = false;

function initChatbot() {
  const floatBtn = document.getElementById('chatbot-float-btn');
  const widget   = document.getElementById('chatbot-widget');
  const closeBtn = document.getElementById('chatbot-close');
  const input    = document.getElementById('chatbot-input');
  const sendBtn  = document.getElementById('chatbot-send');
  const msgArea  = document.getElementById('chatbot-messages');

  if (floatBtn) floatBtn.addEventListener('click', () => {
    widgetOpen = !widgetOpen;
    widget?.classList.toggle('open', widgetOpen);
    floatBtn.textContent = widgetOpen ? '✕' : '🤖';
    if (widgetOpen && msgArea?.children.length === 0) appendBot(getWelcomeMsg());
  });

  if (closeBtn) closeBtn.addEventListener('click', () => {
    widgetOpen = false;
    widget?.classList.remove('open');
    if (floatBtn) floatBtn.textContent = '🤖';
  });

  if (sendBtn) sendBtn.addEventListener('click', sendMessage);
  if (input)   input.addEventListener('keypress', e => { if (e.key === 'Enter') sendMessage(); });
}

function getWelcomeMsg() {
  const lang = window.getCurrentLang ? window.getCurrentLang() : 'en';
  if (lang === 'hi') return 'नमस्ते! मैं भारत बॉट हूँ। मुझसे चुनाव प्रक्रिया, EVM, मतदाता पंजीकरण के बारे में पूछें। 🇮🇳';
  if (lang === 'mr') return 'नमस्कार! मी भारत बॉट आहे. मला निवडणूक प्रक्रिया, EVM, मतदार नोंदणीबद्दल विचारा. 🇮🇳';
  return 'Namaste! I am Bharat Bot 🤖🇮🇳. Ask me about the Indian election process, voter registration, EVMs, or polling booths!';
}

function appendBot(text) {
  const area = document.getElementById('chatbot-messages');
  if (!area) return;
  const div = document.createElement('div');
  div.className = 'chat-bubble bot chat-msg';
  div.textContent = text;
  area.appendChild(div);
  area.scrollTop = area.scrollHeight;
}
function appendUser(text) {
  const area = document.getElementById('chatbot-messages');
  if (!area) return;
  const div = document.createElement('div');
  div.className = 'chat-bubble user chat-msg';
  div.textContent = text;
  area.appendChild(div);
  area.scrollTop = area.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById('chatbot-input');
  if (!input || !input.value.trim()) return;
  const msg = input.value.trim();
  input.value = '';
  appendUser(msg);
  const typing = document.createElement('div');
  typing.className = 'chat-bubble bot';
  typing.innerHTML = '<span class="spinner" style="width:18px;height:18px;margin:0;display:inline-block;"></span>';
  document.getElementById('chatbot-messages')?.appendChild(typing);

  try {
    const lang = window.getCurrentLang ? window.getCurrentLang() : 'en';
    const res = await fetch(API, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ message: msg, language: lang, session_id: sessionId })
    });
    const data = await res.json();
    typing.remove();
    appendBot(data.response || 'Sorry, something went wrong.');
  } catch (err) {
    typing.remove();
    appendBot('Network error. Please try again.');
  }
}

document.addEventListener('DOMContentLoaded', initChatbot);

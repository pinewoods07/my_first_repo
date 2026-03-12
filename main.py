import streamlit as st
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>성간비행모금회 - 우리는 얻다 300만원!</title>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Jua&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  @keyframes rainbow-bg {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  @keyframes bounce {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-20px) scale(1.1); }
  }
  @keyframes shake {
    0%, 100% { transform: rotate(0deg); }
    20% { transform: rotate(-5deg); }
    40% { transform: rotate(5deg); }
    60% { transform: rotate(-3deg); }
    80% { transform: rotate(3deg); }
  }
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
  }
  @keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33% { transform: translateY(-15px) rotate(5deg); }
    66% { transform: translateY(5px) rotate(-3deg); }
  }
  @keyframes marquee {
    0% { transform: translateX(100vw); }
    100% { transform: translateX(-150%); }
  }
  @keyframes zoom {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.3); }
  }
  @keyframes cursor-blink {
    0%, 100% { border-color: transparent; }
    50% { border-color: red; }
  }

  body {
    font-family: 'Jua', cursive;
    background: linear-gradient(270deg, #ff0000, #ff7700, #ffff00, #00ff00, #0000ff, #8b00ff, #ff0000);
    background-size: 1400% 1400%;
    animation: rainbow-bg 3s ease infinite;
    min-height: 100vh;
    cursor: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><text y='28' font-size='28'>⭐</text></svg>") 16 16, auto;
  }

  /* 상단 알림 띠 */
  .ticker-wrap {
    background: black;
    color: yellow;
    font-size: 20px;
    padding: 8px 0;
    overflow: hidden;
    white-space: nowrap;
    border-bottom: 4px solid red;
    border-top: 4px solid red;
  }
  .ticker {
    display: inline-block;
    animation: marquee 12s linear infinite;
  }

  /* 헤더 */
  .header {
    text-align: center;
    padding: 30px 20px 10px;
    position: relative;
  }
  .title-box {
    background: white;
    border: 6px solid black;
    display: inline-block;
    padding: 18px 40px;
    box-shadow: 10px 10px 0 black;
    transform: rotate(-2deg);
    position: relative;
  }
  .title-box h1 {
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(28px, 6vw, 60px);
    color: #e00;
    text-shadow: 4px 4px 0 yellow, 6px 6px 0 blue;
    letter-spacing: -1px;
  }
  .title-box .sub {
    font-size: 18px;
    color: #333;
    animation: blink 1s infinite;
    margin-top: 4px;
  }

  /* 메인 별 마스코트 */
  .mascot-area {
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 20px;
    flex-wrap: wrap;
  }
  .star-alien {
    font-size: 80px;
    display: inline-block;
    filter: drop-shadow(4px 4px 0px black);
    cursor: pointer;
    user-select: none;
  }
  .star-alien:nth-child(1) { animation: float 2.0s ease-in-out infinite; }
  .star-alien:nth-child(2) { animation: bounce 1.5s ease-in-out infinite; }
  .star-alien:nth-child(3) { animation: float 2.5s ease-in-out infinite 0.3s; }
  .star-alien:nth-child(4) { animation: bounce 1.8s ease-in-out infinite 0.5s; }
  .star-alien:nth-child(5) { animation: float 2.2s ease-in-out infinite 0.8s; }

  /* 말풍선 */
  .speech-container {
    text-align: center;
    padding: 10px 20px;
  }
  .speech-bubble {
    background: white;
    border: 5px solid black;
    border-radius: 20px;
    display: inline-block;
    padding: 16px 30px;
    font-size: clamp(16px, 3vw, 22px);
    position: relative;
    box-shadow: 5px 5px 0 black;
    max-width: 700px;
    animation: shake 3s ease-in-out infinite;
  }
  .speech-bubble::after {
    content: '▲';
    position: absolute;
    bottom: -28px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 28px;
    color: black;
  }

  /* 큰 슬로건 */
  .slogan {
    text-align: center;
    padding: 30px 20px;
  }
  .slogan h2 {
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(30px, 7vw, 80px);
    color: white;
    text-shadow: 4px 4px 0 black, 8px 8px 0 red;
    animation: zoom 2s ease-in-out infinite;
    display: inline-block;
  }

  /* 소개 카드들 */
  .cards {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    padding: 20px;
    max-width: 1100px;
    margin: 0 auto;
  }
  .card {
    background: white;
    border: 5px solid black;
    padding: 20px;
    width: 280px;
    box-shadow: 8px 8px 0 black;
    text-align: center;
    font-size: 15px;
    line-height: 1.7;
  }
  .card:nth-child(1) { transform: rotate(-3deg); background: #fffbe6; }
  .card:nth-child(2) { transform: rotate(2deg); background: #e6f7ff; }
  .card:nth-child(3) { transform: rotate(-1.5deg); background: #fff0f6; }
  .card-title {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 22px;
    margin-bottom: 10px;
    border-bottom: 3px solid black;
    padding-bottom: 8px;
  }
  .card-emoji { font-size: 40px; margin-bottom: 10px; display: block; animation: bounce 2s infinite; }

  /* 모금 현황 바 */
  .progress-section {
    max-width: 700px;
    margin: 20px auto;
    padding: 20px;
    background: white;
    border: 6px solid black;
    box-shadow: 10px 10px 0 black;
    text-align: center;
    transform: rotate(1deg);
  }
  .progress-title {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 26px;
    margin-bottom: 12px;
    animation: blink 0.8s infinite;
    color: red;
  }
  .progress-bar-wrap {
    background: #ddd;
    border: 4px solid black;
    border-radius: 20px;
    height: 50px;
    overflow: hidden;
    position: relative;
  }
  .progress-bar-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #ff0080, #ff8c00, #ffe400, #00ff80, #00c8ff, #a855f7);
    background-size: 200% 100%;
    animation: rainbow-bg 1s linear infinite;
    border-radius: 16px;
    transition: width 2s ease;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 10px;
    font-weight: bold;
    font-size: 18px;
    color: white;
    text-shadow: 1px 1px 0 black;
  }
  .progress-label {
    margin-top: 10px;
    font-size: 18px;
  }
  .big-amount {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 36px;
    color: #e00;
    text-shadow: 2px 2px 0 black;
  }

  /* 후원 버튼 */
  .donate-section {
    text-align: center;
    padding: 30px 20px;
  }
  .donate-btn {
    background: red;
    color: white;
    font-family: 'Black Han Sans', sans-serif;
    font-size: clamp(20px, 4vw, 36px);
    padding: 20px 50px;
    border: 5px solid black;
    box-shadow: 8px 8px 0 black;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    position: relative;
    transition: transform 0.1s, box-shadow 0.1s;
    animation: shake 4s ease-in-out infinite;
  }
  .donate-btn:hover {
    transform: translate(4px, 4px);
    box-shadow: 4px 4px 0 black;
    background: darkred;
  }
  .donate-btn:active {
    transform: translate(8px, 8px);
    box-shadow: 0px 0px 0 black;
  }

  /* 후원 레벨 */
  .levels {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
  }
  .levels h3 {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 30px;
    text-align: center;
    color: white;
    text-shadow: 3px 3px 0 black;
    margin-bottom: 20px;
  }
  .level-list {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    justify-content: center;
  }
  .level-item {
    background: white;
    border: 4px solid black;
    padding: 16px 24px;
    box-shadow: 6px 6px 0 black;
    text-align: center;
    min-width: 170px;
  }
  .level-item:nth-child(1) { transform: rotate(-2deg); }
  .level-item:nth-child(2) { transform: rotate(2deg); }
  .level-item:nth-child(3) { transform: rotate(-1deg); }
  .level-item:nth-child(4) { transform: rotate(3deg); }
  .level-price {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 22px;
    color: red;
  }
  .level-reward { font-size: 13px; margin-top: 6px; color: #444; }

  /* 간증 섹션 */
  .testimonials {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
  }
  .testimonials h3 {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 28px;
    text-align: center;
    color: white;
    text-shadow: 3px 3px 0 black;
    margin-bottom: 16px;
  }
  .testi-list {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    justify-content: center;
  }
  .testi-item {
    background: #fffff0;
    border: 4px solid black;
    padding: 16px;
    max-width: 260px;
    box-shadow: 5px 5px 0 black;
  }
  .testi-item:nth-child(1) { transform: rotate(-2deg); }
  .testi-item:nth-child(2) { transform: rotate(1deg); }
  .testi-item:nth-child(3) { transform: rotate(-1.5deg); }
  .testi-star { font-size: 20px; color: gold; }
  .testi-name { font-weight: bold; margin-top: 8px; font-size: 14px; }

  /* 하단 */
  .footer {
    background: black;
    color: white;
    text-align: center;
    padding: 24px;
    font-size: 13px;
    line-height: 2;
    margin-top: 30px;
  }
  .footer .star-logo {
    font-size: 40px;
    animation: spin 3s linear infinite;
    display: inline-block;
  }

  /* 플로팅 별들 */
  .floating-stars { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 999; overflow: hidden; }
  .fstar {
    position: absolute;
    font-size: 24px;
    opacity: 0.7;
    animation: float 4s ease-in-out infinite;
  }

  /* 팝업 배너 */
  .popup-banner {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: yellow;
    border: 5px solid black;
    box-shadow: 6px 6px 0 black;
    padding: 16px 20px;
    z-index: 1000;
    max-width: 240px;
    text-align: center;
    font-size: 14px;
    animation: bounce 2s ease-in-out infinite;
  }
  .popup-banner strong {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 18px;
    display: block;
    margin-bottom: 6px;
    color: red;
  }
  .popup-close {
    position: absolute;
    top: -12px;
    right: -12px;
    background: red;
    color: white;
    border: 3px solid black;
    border-radius: 50%;
    width: 28px;
    height: 28px;
    cursor: pointer;
    font-weight: bold;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* 클릭 폭발 */
  .click-effect {
    position: fixed;
    pointer-events: none;
    font-size: 30px;
    animation: zoom 0.6s ease-out forwards;
    z-index: 9999;
    opacity: 0;
  }
  @keyframes explode {
    0% { transform: scale(0.5); opacity: 1; }
    100% { transform: scale(2.5); opacity: 0; }
  }
  .click-effect { animation: explode 0.6s ease-out forwards; }
</style>
</head>
<body>

<!-- 플로팅 별 -->
<div class="floating-stars" id="floatingStars"></div>

<!-- 팝업 배너 -->
<div class="popup-banner" id="popupBanner">
  <div class="popup-close" onclick="document.getElementById('popupBanner').style.display='none'">✕</div>
  <strong>🚨 긴급 알림 🚨</strong>
  별이 지금 우주에서 길을 잃었음!!<br>
  빨리 돈을 주어야 한다!!!!
</div>

<!-- 상단 띠 -->
<div class="ticker-wrap">
  <span class="ticker">⭐ 우리는 별이다 ⭐ 우리는 우주를 원하다 ⭐ 당신은 좋은 사람임 ⭐ 지금 바로 클릭하라 ⭐ 별들이 배가 고프다 ⭐ 300만원은 적은 금액임 ⭐ 성간비행모금회를 믿어라 ⭐ 우리는 얻다 300만원!! ⭐ &nbsp;&nbsp;&nbsp;&nbsp;</span>
</div>

<!-- 헤더 -->
<div class="header">
  <div class="title-box">
    <h1>⭐ 성간비행모금회 ⭐</h1>
    <div class="sub">✨ STAR ALIEN GALAXY FUND ORGANIZATION ✨ (공식임)</div>
  </div>
</div>

<!-- 마스코트 -->
<div class="mascot-area">
  <span class="star-alien" title="나는 별임">⭐</span>
  <span class="star-alien" title="나도 별임">🌟</span>
  <span class="star-alien" title="우리 대장 별">💫</span>
  <span class="star-alien" title="아기 별">✨</span>
  <span class="star-alien" title="뚱뚱한 별">⭐</span>
</div>

<!-- 말풍선 -->
<div class="speech-container">
  <div class="speech-bubble">
    🗣️ "안녕하세요 인간 여러분! 나는 별 외계인입니다. 나는 우주 여행을 원하다. 하지만 나는 돈이 없다. 당신은 나를 도와야 한다. 감사합니다 매우 많이."
  </div>
</div>

<!-- 큰 슬로건 -->
<div class="slogan">
  <h2>🌈 우리는 얻다 300만원! 🌈</h2>
</div>

<!-- 소개 카드 -->
<div class="cards">
  <div class="card">
    <span class="card-emoji">🚀</span>
    <div class="card-title">우리의 목적</div>
    우리는 성간 여행을 하고 싶다.<br>
    성간 이란 별과 별 사이를 말하다.<br>
    현재 우리는 돈이 <strong>없다.</strong><br>
    그래서 당신에게 요청함.<br>
    <br>
    <em>(이것은 사기가 아님!!)</em>
  </div>
  <div class="card">
    <span class="card-emoji">💸</span>
    <div class="card-title">돈의 사용처</div>
    • 로켓 연료 구매<br>
    • 별 간식 구매 (중요!)<br>
    • 우주복 수선<br>
    • 성간지도 구매<br>
    • 대장 별 새 모자 구매<br>
    <br>
    <em>전부 매우 중요하다.</em>
  </div>
  <div class="card">
    <span class="card-emoji">👽</span>
    <div class="card-title">우리에 대하여</div>
    성간비행모금회는 2024년에<br>
    별 외계인 17명이 설립하다.<br>
    우리의 본부는 오리온자리에<br>
    위치하다. 지구에서는<br>
    서울 어딘가에 있다.<br>
    <br>
    <em>(정확한 주소 모름)</em>
  </div>
</div>

<!-- 모금 현황 -->
<div style="display:flex;justify-content:center;padding:10px 20px;">
  <div class="progress-section">
    <div class="progress-title">🔴 모금 현황 (실시간!!) 🔴</div>
    <div class="progress-bar-wrap">
      <div class="progress-bar-fill" id="progressBar">
        <span id="progressText">0%</span>
      </div>
    </div>
    <div class="progress-label">
      현재 모금액: <span class="big-amount" id="currentAmt">0</span>원
      <br>
      목표: <span class="big-amount">3,000,000</span>원
      <br><br>
      <span style="font-size:13px; color:#666;">※ 이 숫자는 실제가 아님. 하지만 느낌은 실제임.</span>
    </div>
  </div>
</div>

<!-- 후원 버튼 -->
<div class="donate-section">
  <button class="donate-btn" onclick="onDonate()">
    💰 지금 바로 후원하라 💰
  </button>
  <br><br>
  <small style="color:white; text-shadow:1px 1px 0 black; font-size:16px;">
    ※ 버튼을 누르면 별이 기뻐함 (과학적으로 증명됨)
  </small>
</div>

<!-- 후원 등급 -->
<div class="levels">
  <h3>🏆 후원 등급표 (매우 공식) 🏆</h3>
  <div class="level-list">
    <div class="level-item">
      <div>⭐</div>
      <div class="level-price">1,000원</div>
      <div class="level-reward">별에게 감사함을 느낌<br><em>"당신은 좋은 사람"</em> 칭호</div>
    </div>
    <div class="level-item">
      <div>🌟</div>
      <div class="level-price">10,000원</div>
      <div class="level-reward">별이 당신을 기억함<br>이름을 별에 새김<br><em>(소행성 표면)</em></div>
    </div>
    <div class="level-item">
      <div>💫</div>
      <div class="level-price">100,000원</div>
      <div class="level-reward">별의 친구가 됨<br>우주여행시 손 흔들어줌<br><em>"VIP 별 친구" 칭호</em></div>
    </div>
    <div class="level-item">
      <div>🌠</div>
      <div class="level-price">300만원</div>
      <div class="level-reward">우리가 목표 달성함!!<br>대장 별이 직접 춤춤<br><em>"신" 칭호 부여</em></div>
    </div>
  </div>
</div>

<!-- 간증 -->
<div class="testimonials" style="margin-top:10px;">
  <h3>💬 후원자 간증 (모두 실제임) 💬</h3>
  <div class="testi-list">
    <div class="testi-item">
      <div class="testi-star">⭐⭐⭐⭐⭐</div>
      <p>"나는 1000원 후원하다. 그 다음 날 로또 당첨되다. 우연인지 모름. 하지만 아마도 별 덕분이다."</p>
      <div class="testi-name">— 김철수님 (서울 거주, 별의 친구)</div>
    </div>
    <div class="testi-item">
      <div class="testi-star">⭐⭐⭐⭐⭐</div>
      <p>"나는 처음에 사기인줄 알다. 하지만 아니었다. 아마도. 별이 꿈에 나와서 감사하다고 말하다."</p>
      <div class="testi-name">— 이영희님 (별 5개 줌)</div>
    </div>
    <div class="testi-item">
      <div class="testi-star">⭐⭐⭐⭐⭐</div>
      <p>"10만원 후원하니 별이 손 흔들어줌. 우주에서. 어떻게 봤냐고? 꿈임. 하지만 진짜 같았다."</p>
      <div class="testi-name">— ⭐박⭐민⭐준님 (VIP 별 친구)</div>
    </div>
  </div>
</div>

<!-- FAQ -->
<div style="max-width:700px;margin:20px auto;padding:20px;background:white;border:5px solid black;box-shadow:8px 8px 0 black;transform:rotate(-1deg);">
  <div style="font-family:'Black Han Sans',sans-serif;font-size:24px;margin-bottom:12px;text-align:center;">❓ 자주 묻는 질문 ❓</div>

  <p><strong>Q: 이게 진짜임?</strong><br>
  A: 네. 매우 진짜임. 의심하지 말아라.</p><br>

  <p><strong>Q: 별 외계인이 실제로 존재하나?</strong><br>
  A: 이 질문은 무례하다. 우리는 지금 여기 있다.</p><br>

  <p><strong>Q: 돈을 어디로 보내나?</strong><br>
  A: 우주 계좌로 이체하다. 주소는 오리온자리 3번 별 옆</p><br>

  <p><strong>Q: 300만원 모으면 진짜 우주 여행하나?</strong><br>
  A: 당연히 그렇다. 아마도. 가능성 있다.</p><br>

  <p><strong>Q: 환불 되나?</strong><br>
  A: 별은 환불을 이해하지 못하다. 미안하다.</p>
</div>

<!-- 하단 -->
<div class="footer">
  <div class="star-logo">⭐</div>
  <br>
  <strong>성간비행모금회 (STAR ALIEN GALAXY FUND ORG.)</strong><br>
  본부 위치: 오리온자리 | 지구 지부: 서울 어딘가<br>
  대표: 대장별 (이름 없음, 별이니까)<br>
  사업자번호: ⭐⭐⭐-⭐⭐-⭐⭐⭐⭐⭐<br>
  문의: star@star.star (응답 안 할 수도 있음)<br>
  <br>
  <small>© 2024 성간비행모금회. 모든 권리는 별에게 있다.<br>
  이 웹사이트를 보는 것만으로도 후원 의사가 있는 것으로 간주한다. (농담임. 아마도.)</small>
</div>

<script>
  // 플로팅 별 생성
  const container = document.getElementById('floatingStars');
  const emojis = ['⭐','🌟','✨','💫','🌠'];
  for (let i = 0; i < 15; i++) {
    const s = document.createElement('div');
    s.className = 'fstar';
    s.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    s.style.left = Math.random() * 100 + 'vw';
    s.style.top = Math.random() * 100 + 'vh';
    s.style.animationDelay = (Math.random() * 4) + 's';
    s.style.animationDuration = (3 + Math.random() * 3) + 's';
    s.style.fontSize = (16 + Math.random() * 20) + 'px';
    container.appendChild(s);
  }

  // 모금 바 애니메이션
  let currentAmt = 0;
  const targetAmt = 1234567;
  const maxAmt = 3000000;
  setTimeout(() => {
    const bar = document.getElementById('progressBar');
    const pct = Math.round(targetAmt / maxAmt * 100);
    bar.style.width = pct + '%';
    bar.querySelector('#progressText').textContent = pct + '%';
    let n = 0;
    const inc = Math.ceil(targetAmt / 80);
    const interval = setInterval(() => {
      n = Math.min(n + inc, targetAmt);
      document.getElementById('currentAmt').textContent = n.toLocaleString('ko-KR');
      if (n >= targetAmt) clearInterval(interval);
    }, 25);
  }, 500);

  // 별 클릭 효과
  document.querySelectorAll('.star-alien').forEach(el => {
    el.addEventListener('click', function() {
      const msgs = ['감사하다!!', '나는 기쁘다!', '우주!!', '돈 주어라!', '별 만세!!'];
      alert(msgs[Math.floor(Math.random() * msgs.length)]);
    });
  });

  // 후원 버튼
  let donateCount = 0;
  function onDonate() {
    donateCount++;
    const msgs = [
      '결제 창을 열려고 했지만\n별이 아직 우주 계좌를 만들지 않았다.\n미안하다. 나중에 다시 클릭하라.',
      '와!! 당신은 ' + donateCount + '번 클릭했다!\n별이 매우 감동받다!\n하지만 아직 결제 안 됨.',
      '시스템 오류 발생\n(오류 코드: 별☆404)\n별이 로켓 수리 중이라 바쁘다.',
      '지금 처리 중...\n.\n..\n...\n아직 처리 중...\n별이 느리다. 기다려라.',
      '이 버튼은 사실 장식임.\n진짜 후원은 별을 직접 만나야 함.\n별의 위치: 오리온자리'
    ];
    alert(msgs[(donateCount - 1) % msgs.length]);
  }

  // 클릭 시 별 터짐 효과
  document.addEventListener('click', function(e) {
    const el = document.createElement('div');
    el.className = 'click-effect';
    el.textContent = ['⭐','✨','💫','🌟'][Math.floor(Math.random()*4)];
    el.style.left = (e.clientX - 20) + 'px';
    el.style.top = (e.clientY - 20) + 'px';
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 700);
  });

  // 제목 클릭 흔들기
  document.querySelector('.title-box').addEventListener('click', function() {
    this.style.animation = 'shake 0.4s';
    setTimeout(() => this.style.animation = '', 400);
  });
</script>
</body>
</html>

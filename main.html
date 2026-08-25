<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <!-- 모바일 화면에 맞추고 확대/축소 방지 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>별빛 벽돌깨기</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: #0f172a; /* 짙은 남색 밤하늘 배경 */
            color: #f8fafc;
            font-family: 'Noto Sans KR', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden; /* 모바일 스크롤 방지 */
        }

        #game-container {
            position: relative;
            width: 100%;
            max-width: 480px; /* PC에서는 최대 480px로 제한 */
            padding: 10px;
        }

        canvas {
            background: linear-gradient(to bottom, #1e293b, #0f172a);
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(253, 224, 71, 0.1);
            display: block;
            width: 100%;
            height: auto;
            touch-action: none; /* 캔버스 위에서 브라우저 기본 터치 액션 막기 */
        }

        #ui-layer {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            pointer-events: none; /* UI 레이어는 클릭을 통과시킴 */
        }

        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #fde047;
            text-shadow: 0 0 10px rgba(253, 224, 71, 0.5);
        }

        .btn {
            pointer-events: auto; /* 버튼은 클릭 가능하게 */
            background-color: #3b82f6;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: transform 0.1s, background-color 0.2s;
        }

        .btn:active {
            transform: scale(0.95);
        }

        #start-btn { display: block; }
        #game-over { display: none; text-align: center; }
        #game-over h2 { margin-bottom: 15px; color: #ef4444; }
        #game-clear { display: none; text-align: center; }
        #game-clear h2 { margin-bottom: 15px; color: #4ade80; }
    </style>
</head>
<body>

    <div id="game-container">
        <!-- 내부 해상도는 480x640 고정, CSS로 화면에 맞게 스케일링 -->
        <canvas id="gameCanvas" width="480" height="640"></canvas>
        
        <div id="ui-layer">
            <div id="start-screen">
                <h1>🌟 별빛 벽돌깨기</h1>
                <button class="btn" id="start-btn">게임 시작</button>
            </div>
            
            <div id="game-over">
                <h2>Game Over</h2>
                <button class="btn" id="restart-btn">다시 하기</button>
            </div>

            <div id="game-clear">
                <h2>Clear! ✨</h2>
                <button class="btn" id="next-btn">다시 하기</button>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        // UI 요소
        const startScreen = document.getElementById('start-screen');
        const gameOverScreen = document.getElementById('game-over');
        const gameClearScreen = document.getElementById('game-clear');
        const startBtn = document.getElementById('start-btn');
        const restartBtn = document.getElementById('restart-btn');
        const nextBtn = document.getElementById('next-btn');

        // 게임 변수 세팅
        let animationId;
        let isPlaying = false;
        let score = 0;
        let lives = 3;

        // 패들 속성
        const paddleHeight = 12;
        const paddleWidth = 90;
        let paddleX = (canvas.width - paddleWidth) / 2;

        // 별(공) 속성
        const starRadius = 8; // 충돌 판정용 반지름
        let x = canvas.width / 2;
        let y = canvas.height - 30;
        let dx = 4;
        let dy = -4;
        let starRotation = 0;

        // 벽돌 속성
        const brickRowCount = 5;
        const brickColumnCount = 7;
        const brickWidth = 56;
        const brickHeight = 20;
        const brickPadding = 10;
        const brickOffsetTop = 60;
        const brickOffsetLeft = 14;
        const brickColors = ['#f43f5e', '#f97316', '#eab308', '#22c55e', '#06b6d4'];

        let bricks = [];
        
        function initBricks() {
            bricks = [];
            for(let c=0; c<brickColumnCount; c++) {
                bricks[c] = [];
                for(let r=0; r<brickRowCount; r++) {
                    bricks[c][r] = { x: 0, y: 0, status: 1 };
                }
            }
        }

        // 별 그리기 함수 (공 대신 사용)
        function drawStar(cx, cy, spikes, outerRadius, innerRadius, angle) {
            let rot = Math.PI / 2 * 3 + angle;
            let step = Math.PI / spikes;
            
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(cx + Math.cos(rot) * outerRadius, cy + Math.sin(rot) * outerRadius);
            
            for (let i = 0; i < spikes; i++) {
                ctx.lineTo(cx + Math.cos(rot) * outerRadius, cy + Math.sin(rot) * outerRadius);
                rot += step;
                ctx.lineTo(cx + Math.cos(rot) * innerRadius, cy + Math.sin(rot) * innerRadius);
                rot += step;
            }
            
            ctx.lineTo(cx + Math.cos(rot) * outerRadius, cy + Math.sin(rot) * outerRadius);
            ctx.closePath();
            
            // 별 색상 및 빛나는 효과
            ctx.fillStyle = '#fde047';
            ctx.shadowBlur = 10;
            ctx.shadowColor = '#fde047';
            ctx.fill();
            ctx.restore();
        }

        // 패들 그리기
        function drawPaddle() {
            ctx.beginPath();
            ctx.roundRect(paddleX, canvas.height - paddleHeight - 10, paddleWidth, paddleHeight, 6);
            ctx.fillStyle = '#38bdf8';
            ctx.shadowBlur = 10;
            ctx.shadowColor = '#38bdf8';
            ctx.fill();
            ctx.closePath();
            ctx.shadowBlur = 0; // 초기화
        }

        // 벽돌 그리기
        function drawBricks() {
            for(let c=0; c<brickColumnCount; c++) {
                for(let r=0; r<brickRowCount; r++) {
                    if(bricks[c][r].status === 1) {
                        let brickX = (c * (brickWidth + brickPadding)) + brickOffsetLeft;
                        let brickY = (r * (brickHeight + brickPadding)) + brickOffsetTop;
                        bricks[c][r].x = brickX;
                        bricks[c][r].y = brickY;
                        
                        ctx.beginPath();
                        ctx.roundRect(brickX, brickY, brickWidth, brickHeight, 4);
                        ctx.fillStyle = brickColors[r];
                        ctx.fill();
                        ctx.closePath();
                    }
                }
            }
        }

        // 점수 및 목숨 그리기
        function drawScore() {
            ctx.font = "16px 'Noto Sans KR'";
            ctx.fillStyle = "#cbd5e1";
            ctx.fillText("점수: " + score, 15, 25);
            ctx.fillText("목숨: " + "❤️".repeat(lives), canvas.width - 90, 25);
        }

        // 충돌 감지
        function collisionDetection() {
            for(let c=0; c<brickColumnCount; c++) {
                for(let r=0; r<brickRowCount; r++) {
                    let b = bricks[c][r];
                    if(b.status === 1) {
                        if(x > b.x && x < b.x + brickWidth && y > b.y && y < b.y + brickHeight) {
                            dy = -dy;
                            b.status = 0;
                            score += 10;
                            
                            // 클리어 체크
                            if(score === brickRowCount * brickColumnCount * 10) {
                                gameWin();
                            }
                        }
                    }
                }
            }
        }

        // 마우스 및 터치 입력 처리 (반응형 대응)
        function updatePaddlePosition(clientX) {
            const rect = canvas.getBoundingClientRect();
            // CSS로 축소/확대된 캔버스의 비율 계산
            const scaleX = canvas.width / rect.width; 
            const relativeX = (clientX - rect.left) * scaleX;
            
            if(relativeX > 0 && relativeX < canvas.width) {
                paddleX = relativeX - paddleWidth / 2;
                // 화면 밖으로 나가지 않게 보정
                if (paddleX < 0) paddleX = 0;
                if (paddleX + paddleWidth > canvas.width) paddleX = canvas.width - paddleWidth;
            }
        }

        // PC 마우스 컨트롤
        document.addEventListener("mousemove", (e) => {
            if(isPlaying) updatePaddlePosition(e.clientX);
        }, false);

        // 모바일 터치 컨트롤
        canvas.addEventListener("touchmove", (e) => {
            if(isPlaying) {
                e.preventDefault(); // 화면 스크롤 방지
                updatePaddlePosition(e.touches[0].clientX);
            }
        }, { passive: false });

        // 메인 게임 루프
        function draw() {
            if(!isPlaying) return;

            // 캔버스 지우기
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            drawBricks();
            // 5각 별 그리기 (중심x, 중심y, 꼭짓점수, 외부반지름, 내부반지름, 회전각도)
            drawStar(x, y, 5, 12, 5, starRotation);
            drawPaddle();
            drawScore();
            collisionDetection();

            // 별 회전 애니메이션
            starRotation += 0.05;

            // 좌우 벽 충돌
            if(x + dx > canvas.width - starRadius || x + dx < starRadius) {
                dx = -dx;
            }
            
            // 윗벽 충돌
            if(y + dy < starRadius) {
                dy = -dy;
            } 
            // 바닥 충돌
            else if(y + dy > canvas.height - starRadius - paddleHeight - 10) {
                // 패들에 닿았는지 확인
                if(x > paddleX && x < paddleX + paddleWidth) {
                    // 패들의 어느 부분에 맞았는지에 따라 각도 변경 (가운데일수록 수직, 끝일수록 대각선)
                    let hitPoint = x - (paddleX + paddleWidth / 2);
                    dx = hitPoint * 0.15;
                    dy = -dy;
                } 
                else if(y + dy > canvas.height - starRadius) {
                    lives--;
                    if(!lives) {
                        gameOver();
                    } else {
                        // 위치 초기화
                        x = canvas.width / 2;
                        y = canvas.height - 30;
                        dx = 4;
                        dy = -4;
                        paddleX = (canvas.width - paddleWidth) / 2;
                    }
                }
            }

            x += dx;
            y += dy;

            animationId = requestAnimationFrame(draw);
        }

        // 게임 상태 관리 함수들
        function startGame() {
            startScreen.style.display = 'none';
            gameOverScreen.style.display = 'none';
            gameClearScreen.style.display = 'none';
            
            initBricks();
            score = 0;
            lives = 3;
            x = canvas.width / 2;
            y = canvas.height - 30;
            dx = 4;
            dy = -4;
            paddleX = (canvas.width - paddleWidth) / 2;
            
            isPlaying = true;
            draw();
        }

        function gameOver() {
            isPlaying = false;
            cancelAnimationFrame(animationId);
            gameOverScreen.style.display = 'block';
        }

        function gameWin() {
            isPlaying = false;
            cancelAnimationFrame(animationId);
            gameClearScreen.style.display = 'block';
        }

        // 버튼 이벤트 리스너
        startBtn.addEventListener('click', startGame);
        restartBtn.addEventListener('click', startGame);
        nextBtn.addEventListener('click', startGame);

        // 초기 화면 세팅
        initBricks();
        drawBricks();
        drawPaddle();
        drawStar(canvas.width/2, canvas.height-30, 5, 12, 5, 0);

    </script>
</body>
</html>

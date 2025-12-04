window.addEventListener("scroll", () => {
    const black = document.querySelector(".blackcont");
    const imgs = document.querySelectorAll(".images_cont img");

    const blackTop = black.offsetTop;
    const blackHeight = black.offsetHeight;
    const scrollY = window.scrollY;

    // Trigger only inside black section
    if (scrollY > blackTop - window.innerHeight && scrollY < blackTop + blackHeight) {
        const progress = (scrollY - blackTop + window.innerHeight / 2) / blackHeight;

        // Different directions and strengths for each image
        const movements = [
            { dir: -1, dist: 100 },
            { dir: 1, dist: 150 },
            { dir: -1, dist: 70 },
            { dir: 1, dist: 120 },
            { dir: -1, dist: 120 },
        ];

        imgs.forEach((img, i) => {
            const { dir, dist } = movements[i % movements.length];
            const move = dir * progress * dist;
            img.style.transform = `translateY(${move}px)`;
        });
    }
});
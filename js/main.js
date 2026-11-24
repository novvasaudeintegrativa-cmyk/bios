/* Bios Therapy XII — interações da landing page
   - Tabs de artigos científicos
   - Acordeão de FAQ
   - Reveal on scroll
   - Placeholders de vídeo (troque o data-embed pelo <iframe> real)
*/
(function () {
  "use strict";

  /* ---------- Tabs: Artigos Científicos ---------- */
  var tablist = document.querySelector("[data-tabs]");
  if (tablist) {
    var btns = Array.prototype.slice.call(tablist.querySelectorAll(".tabs__btn"));
    var panels = Array.prototype.slice.call(
      document.querySelectorAll("[data-tabpanel]")
    );
    function select(id) {
      btns.forEach(function (b) {
        b.setAttribute("aria-selected", String(b.dataset.tab === id));
      });
      panels.forEach(function (p) {
        p.hidden = p.dataset.tabpanel !== id;
      });
    }
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        select(b.dataset.tab);
      });
    });
    select(btns[0].dataset.tab);
  }

  /* ---------- FAQ acordeão ---------- */
  document.querySelectorAll(".faq__item").forEach(function (item) {
    var q = item.querySelector(".faq__q");
    var a = item.querySelector(".faq__a");
    q.addEventListener("click", function () {
      var open = item.classList.toggle("open");
      q.setAttribute("aria-expanded", String(open));
      a.style.maxHeight = open ? a.scrollHeight + "px" : "0px";
    });
  });

  /* ---------- Vídeo: placeholder -> embed real ---------- */
  document.querySelectorAll(".video").forEach(function (v) {
    var poster = v.getAttribute("data-poster");
    if (poster) {
      v.style.backgroundImage = "url('" + poster + "')";
      v.style.backgroundSize = "cover";
      v.style.backgroundPosition = "center";
    }
    var btn = v.querySelector(".video__play");
    if (!btn) return;
    if (!v.getAttribute("data-embed")) {
      btn.disabled = true;
      btn.setAttribute("aria-disabled", "true");
      return;
    }
    btn.addEventListener("click", function () {
      var embed = v.getAttribute("data-embed");
      var f = document.createElement("iframe");
      f.src = embed;
      f.title = "Vídeo Bios Therapy";
      f.loading = "lazy";
      f.allow =
        "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      f.style.cssText = "position:absolute;inset:0;width:100%;height:100%;border:0";
      v.innerHTML = "";
      v.appendChild(f);
    });
  });

  /* ---------- Reveal on scroll ---------- */
  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  document.querySelectorAll(".reveal").forEach(function (el) {
    io.observe(el);
  });

})();

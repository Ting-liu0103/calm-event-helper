(function () {
  var guides = Array.isArray(window.EVENTPILOT_GUIDES) ? window.EVENTPILOT_GUIDES : [];
  function el(id) { return document.getElementById(id); }

  function card(guide) {
    var article = document.createElement("article");
    article.className = "guide-card";

    var top = document.createElement("div");
    top.className = "card-top";
    var emoji = document.createElement("span");
    emoji.className = "emoji";
    emoji.textContent = guide.emoji;
    var cat = document.createElement("span");
    cat.className = "pill";
    cat.textContent = guide.category;
    top.append(emoji, cat);

    var h3 = document.createElement("h3");
    h3.textContent = guide.title;
    var p = document.createElement("p");
    p.textContent = guide.summary;

    var foot = document.createElement("div");
    foot.className = "card-foot";
    var level = document.createElement("span");
    level.textContent = guide.level;
    var link = document.createElement("a");
    link.href = "./guide.html?id=" + encodeURIComponent(guide.id);
    link.textContent = "查看指南 →";
    foot.append(level, link);

    article.append(top, h3, p, foot);
    return article;
  }

  function initHome() {
    var grid = el("guide-grid");
    var filters = el("category-filters");
    var search = el("search-input");
    if (!grid || !filters || !search) return;

    var active = "全部";
    var keyword = "";
    var categories = ["全部"].concat(Array.from(new Set(guides.map(function (g) { return g.category; }))));

    categories.forEach(function (name) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "filter" + (name === "全部" ? " active" : "");
      btn.textContent = name;
      btn.addEventListener("click", function () {
        active = name;
        filters.querySelectorAll(".filter").forEach(function (x) {
          x.classList.toggle("active", x === btn);
        });
        render();
      });
      filters.appendChild(btn);
    });

    function render() {
      var q = keyword.trim().toLowerCase();
      var list = guides.filter(function (g) {
        var categoryOk = active === "全部" || g.category === active;
        var text = [g.title, g.summary, g.category, g.intro].join(" ").toLowerCase();
        return categoryOk && (!q || text.indexOf(q) >= 0);
      });
      grid.replaceChildren.apply(grid, list.map(card));
      el("result-count").textContent = "顯示 " + list.length + " / " + guides.length + " 篇";
      el("empty-state").hidden = list.length !== 0;
    }

    search.addEventListener("input", function (e) {
      keyword = e.target.value;
      render();
    });

    render();
  }

  function makeList(items, className) {
    var ul = document.createElement("ul");
    ul.className = className;
    items.forEach(function (text) {
      var li = document.createElement("li");
      li.textContent = text;
      ul.appendChild(li);
    });
    return ul;
  }

  function initGuide() {
    var root = el("guide-content");
    if (!root) return;

    var id = new URLSearchParams(location.search).get("id");
    var guide = guides.find(function (g) { return g.id === id; });

    if (!guide) {
      root.hidden = true;
      el("guide-not-found").hidden = false;
      return;
    }

    document.title = guide.title + "｜EventPilot Playbook";

    var hero = document.createElement("section");
    hero.className = "detail-hero";

    var icon = document.createElement("div");
    icon.className = "huge";
    icon.textContent = guide.emoji;

    var meta = document.createElement("div");
    meta.className = "meta";
    meta.textContent = guide.category + "　·　" + guide.level + "　·　更新 " + guide.updatedAt;

    var title = document.createElement("h1");
    title.textContent = guide.title;

    var intro = document.createElement("p");
    intro.textContent = guide.intro;

    hero.append(icon, meta, title, intro);

    var steps = document.createElement("section");
    steps.className = "detail-section";
    var stepsTitle = document.createElement("h2");
    stepsTitle.textContent = "怎麼做？";
    steps.appendChild(stepsTitle);

    guide.steps.forEach(function (s, i) {
      var row = document.createElement("article");
      row.className = "step";

      var no = document.createElement("b");
      no.textContent = String(i + 1).padStart(2, "0");

      var box = document.createElement("div");
      var h3 = document.createElement("h3");
      h3.textContent = s.title;
      var p = document.createElement("p");
      p.textContent = s.description;

      box.append(h3, p);
      row.append(no, box);
      steps.appendChild(row);
    });

    var lower = document.createElement("div");
    lower.className = "lower";

    var c1 = document.createElement("section");
    c1.className = "content-card";
    var t1 = document.createElement("h2");
    t1.textContent = "✅ Checklist";
    c1.append(t1, makeList(guide.checklist, "checklist"));

    var c2 = document.createElement("section");
    c2.className = "content-card";
    var t2 = document.createElement("h2");
    t2.textContent = "💡 容易忽略的提醒";
    c2.append(t2, makeList(guide.tips, "tips"));

    lower.append(c1, c2);
    root.append(hero, steps, lower);
  }

  initHome();
  initGuide();
})();

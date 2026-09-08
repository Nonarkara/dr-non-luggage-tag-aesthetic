/* SPDX-License-Identifier: MIT */
/* Optional. Copy LPN / object id. Absence of JS does not break the package. */
(function () {
  function onClick(event) {
    var btn = event.target.closest("[data-copy]");
    if (!btn) return;
    var value = btn.getAttribute("data-copy");
    if (!value || !navigator.clipboard) return;
    navigator.clipboard.writeText(value).then(function () {
      var prev = btn.getAttribute("data-label") || btn.textContent;
      btn.textContent = "COPIED";
      setTimeout(function () {
        btn.textContent = prev;
      }, 1200);
    });
  }
  document.addEventListener("click", onClick);
})();

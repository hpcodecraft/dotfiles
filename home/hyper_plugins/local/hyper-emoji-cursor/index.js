function createAnimation(chars) {
  let anim = '';
  chars.forEach((char, i) => {
    anim += `
      ${(i / chars.length) * 100}% {
        content: '${char}'
      }`;
  });
  return anim;
}

exports.decorateConfig = (config) => {
  const emojiConfig = Object.assign({
    fontSize: config.fontSize,
    speed: 1000,
    emoji: ['👽', '💀'],
  }, config.emojiCursor);

  return Object.assign({}, config, {
    cursorColor: 'transparent',
    termCSS: `
      ${config.termCSS || ''}
      .cursor-node::after {
        content: '${emojiConfig.emoji[0]}';
        font-size: ${emojiConfig.fontSize}px;
        position: absolute;
        left: 0;
        right: 0;
        top: -50%;
        animation: emoji ${emojiConfig.speed}ms linear infinite;
      }

      @keyframes emoji {
        ${createAnimation(emojiConfig.emoji)}
      }`,
  });
};

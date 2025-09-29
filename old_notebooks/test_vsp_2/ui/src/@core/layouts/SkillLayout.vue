<template>
  <section class="bg-core-bg-secondary flex h-screen flex-col items-start">
    <header class="flex h-14 flex-shrink-0 items-center justify-between self-stretch px-XL py-2.5">
      <div class="flex-row flex items-center gap-2">
        <slot name="title" />
      </div>
      <slot name="header-left" />
    </header>
    <slot />
  </section>
</template>

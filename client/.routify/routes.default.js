// @ts-nocheck


export const routes = {
  "meta": {},
  "id": "_default",
  "name": "",
  "file": {
    "path": "src/routes",
    "dir": "src",
    "base": "routes",
    "ext": "",
    "name": "routes"
  },
  "rootName": "default",
  "routifyDir": import.meta.url,
  "children": [
    {
      "meta": {},
      "id": "_default_ApiTest_svelte",
      "name": "ApiTest",
      "file": {
        "path": "src/routes/ApiTest.svelte",
        "dir": "src/routes",
        "base": "ApiTest.svelte",
        "ext": ".svelte",
        "name": "ApiTest"
      },
      "asyncModule": () => import('../src/routes/ApiTest.svelte'),
      "children": []
    },
    {
      "meta": {
        "isDefault": true
      },
      "id": "_default_index_svelte",
      "name": "index",
      "file": {
        "path": "src/routes/index.svelte",
        "dir": "src/routes",
        "base": "index.svelte",
        "ext": ".svelte",
        "name": "index"
      },
      "asyncModule": () => import('../src/routes/index.svelte'),
      "children": []
    },
    {
      "meta": {},
      "id": "_default_places_svelte",
      "name": "places",
      "file": {
        "path": "src/routes/places.svelte",
        "dir": "src/routes",
        "base": "places.svelte",
        "ext": ".svelte",
        "name": "places"
      },
      "asyncModule": () => import('../src/routes/places.svelte'),
      "children": []
    },
    {
      "meta": {},
      "id": "_default_signup_svelte",
      "name": "signup",
      "file": {
        "path": "src/routes/signup.svelte",
        "dir": "src/routes",
        "base": "signup.svelte",
        "ext": ".svelte",
        "name": "signup"
      },
      "asyncModule": () => import('../src/routes/signup.svelte'),
      "children": []
    },
    {
      "meta": {
        "dynamic": true,
        "dynamicSpread": true,
        "order": false,
        "inline": false
      },
      "name": "[...404]",
      "file": {
        "path": ".routify/components/[...404].svelte",
        "dir": ".routify/components",
        "base": "[...404].svelte",
        "ext": ".svelte",
        "name": "[...404]"
      },
      "asyncModule": () => import('./components/[...404].svelte'),
      "children": []
    }
  ]
}
export default routes
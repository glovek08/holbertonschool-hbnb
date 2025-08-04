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
        "dynamic": true,
        "order": false,
        "dynamicSpread": true,
        "inline": false
      },
      "id": "_default_____404__svelte",
      "name": "[...404]",
      "file": {
        "path": "src/routes/[...404].svelte",
        "dir": "src/routes",
        "base": "[...404].svelte",
        "ext": ".svelte",
        "name": "[...404]"
      },
      "asyncModule": () => import('../src/routes/[...404].svelte'),
      "children": []
    },
    {
      "meta": {},
      "id": "_default_command_center_svelte",
      "name": "command_center",
      "file": {
        "path": "src/routes/command_center.svelte",
        "dir": "src/routes",
        "base": "command_center.svelte",
        "ext": ".svelte",
        "name": "command_center"
      },
      "asyncModule": () => import('../src/routes/command_center.svelte'),
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
      "id": "_default_place_details_svelte",
      "name": "place_details",
      "file": {
        "path": "src/routes/place_details.svelte",
        "dir": "src/routes",
        "base": "place_details.svelte",
        "ext": ".svelte",
        "name": "place_details"
      },
      "asyncModule": () => import('../src/routes/place_details.svelte'),
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
    }
  ]
}
export default routes
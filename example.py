# Copyright 2020 Thiago Teixeira
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from htbuild import div, ul, li, img

image_paths = [
  "http://...",
  "http://...",
  "http://...",
]

out = div(id="container")(
  ul(_class="image-list")(
    [
      li(img(src=image_path, _class="large-image"))
      for image_path in image_paths
    ]
  )
)

print(out)
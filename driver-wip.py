#
# Created on Fri Jul 24 2020
#
# This file is a part of the Python TerrabaseDB driver
#
# Copyright (c) 2020, Sayan Nandan <ohsayan at outlook dot com>
# Licensed under the Apache License, Version 2.0 (the "License");
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from terrabasedb.connector import *

db = Connector()
action = ActionGroup()
action.add("GET")
action.add("x")
db.execute(SimpleQuery(action))
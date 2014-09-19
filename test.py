from backend.util import Util
from b_logic.business import Billetera


print Util.sha1('Martin', 'Persona', 'martin.mantovani@gmail.com', Billetera.PAGAR)
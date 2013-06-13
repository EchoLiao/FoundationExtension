
from NSAttributedStringData import *

interface="""{availableheader}
/*!
 *  @brief Adds {name} attribute value to the characters in the specified range.
 *  @details Generated by {filename}
 */
- (void)addAttribute{Name}:({type}){name} range:(NSRange)range{available};
/*!
 *  @brief Removes {name} attribute from the characters in the specified range.
 *  @details Generated by {filename}
 */
- (void)removeAttribute{Name}FromRange:(NSRange)range{available};
{availablefooter}"""

for prop in props:
    if prop.name.endswith('Array'): continue
    print interface.format(
        type=prop.type,
        name=prop.name,
        Name=prop.Name,
        available=' ' + prop.available_mac if prop.available else '',
        availableheader=prop.available_header if prop.available else '',
        availablefooter='#endif' if prop.available else '',
        filename=__file__,
    )